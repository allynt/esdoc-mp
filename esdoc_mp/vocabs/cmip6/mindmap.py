# -*- coding: utf-8 -*-

"""
.. module:: write_cmip6_xmind.py
   :platform: Unix, Windows
   :synopsis: Rewrites cmip6 vocab defintions to xmind files.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import argparse
import json
import os

import xml.etree.ElementTree as ET

from esdoc_mp.vocabs.cmip6.parser import VocabParser



# Define command line options.
_ARGS = argparse.ArgumentParser("Rewrites CMIP6 vocab definitions to xmind files.")
_ARGS.add_argument(
    "--stylesheet",
    help="Path to a spreadsheet configuration file.",
    dest="stylesheet",
    type=str
    )
_ARGS.add_argument(
    "--dest",
    help="Path to a directory into which xmind defintions will be written.",
    dest="dest",
    type=str
    )
_ARGS.add_argument(
    "--domain",
    help="Domain for whise mindmap file will be written.",
    dest="domain",
    type=str,
    default=None
    )


_NOTES = """
<html>
  <head></head>
  <body>
    <dl>
        {}
    </dl>
  </body>
</html>
"""

_NOTE = "<dt><b>{}</b></dt><dd>{}</dd>"



class _VocabParserConfiguration(object):
    """Wraps access to configuration information stored in associated config file.

    """
    def __init__(self, fpath):
        """Instance constructor.

        """
        with open(fpath, 'r') as f:
            self._data = json.loads(f.read())


    def get_section(self, key):
        """Returns a section within the config file.

        """
        return self._data.get(key, {})


class _VocabParser(VocabParser):
    def __init__(self, domain_filter, stylesheet):
        """Instance constructor.

        """
        super(_VocabParser, self).__init__(domain_filter)
        self.cfg = _VocabParserConfiguration(stylesheet)
        self.maps = {}
        self.nodes = {}
        self.positions = {}


    @property
    def mindmaps(self):
        """Returns set of mindmaps and associated domains.

        """
        return self.maps.values()


    def _set_node(self, parent, owner, text=None, style=None, position=None):
        """Sets a mindmap node.

        """
        # Get section style config.
        cfg = self.cfg.get_section(owner.style_type)

        # Initialise mindmap node attributes.
        atts = {
            'FOLDED': str(cfg['is-collapsed']).lower(),
            'COLOR': cfg['font-color'],
            'BACKGROUND_COLOR': cfg['bg-color'],
            'STYLE': style or "bubble",
            'TEXT': text if text else owner.name
        }

        # Set node url.
        try:
            owner.url
        except AttributeError:
            pass
        else:
            atts['LINK'] = owner.url

        # Set node position (right | left).
        if position:
            atts['POSITION'] = position

        # Get node parent.
        if not isinstance(parent, ET.Element):
            parent = self.nodes[parent]

        # Create new node & cache.
        self.nodes[owner] = ET.SubElement(parent, 'node', atts)

        # Set node font / notes.
        self._set_font(owner)
        self._set_notes(owner)


    def _set_font(self, owner):
        """Styles a node with font information.

        """
        cfg = self.cfg.get_section(owner.style_type)

        ET.SubElement(self.nodes[owner], 'font', {
            'BOLD': str(cfg['font-bold']),
            'NAME': cfg['font-name'],
            'SIZE': str(cfg['font-size'])
            })


    def _set_notes(self, owner):
        """Set notes associated with a node.

        """
        # Skip if owner does not define notes.
        try:
            notes = owner.notes
        except AttributeError:
            return

        # Convert notes to HTML.
        notes = [_NOTE.format(k, v) for k, v in owner.notes]
        notes = _NOTES.format("".join(notes))

        # Inject notes into mindmap.
        content = ET.SubElement(self.nodes[owner], 'richcontent', {"TYPE": "NOTE"})
        content.append(ET.fromstring(notes))


    def on_domain_parse(self, domain):
        """On domain parse event handler.

        """
        self.maps[domain] = ET.Element('map', {})
        self._set_node(self.maps[domain], domain, style="fork")


    def on_process_parse(self, domain, process):
        """On process parse event handler.

        """
        self.positions[process] = 'left' if len(self.positions) % 2 == 0 else 'right'
        self._set_node(domain, process, position=self.positions[process])
        self._set_notes(process)


    def on_subprocess_parse(self, process, subprocess):
        """On sub-process parse event handler.

        """
        self.positions[subprocess] = self.positions[process]
        self._set_node(process, subprocess)


    def on_detail_parse(self, owner, detail):
        """On process detail parse event handler.

        """
        self.positions[detail] = self.positions[owner]
        self._set_node(owner, detail)


    def on_detail_property_parse(self, owner, detail_property):
        """On detail property parse event handler.

        """
        self._set_node(owner, detail_property)
        self._set_notes(detail_property)
        for choice in detail_property.choices:
            self._set_node(detail_property, choice, text=choice.value)


def _main(args):
    """Main entry point.

    """
    # Extract input args.
    domain = args.domain if args.domain not in {"*", "all"} else None
    stylesheet = args.stylesheet

    # Perform a vocab parse in order to create mindmaps.
    parser = _VocabParser(domain, stylesheet)
    parser.parse()

    # Write mindmaps to file system.
    for domain, mindmap in parser.maps.items():
        fpath = os.path.join(args.dest, "{}.mm".format(domain.id))
        with open(fpath, 'w') as f:
            f.write(ET.tostring(mindmap))


# Entry point.
if __name__ == '__main__':
    _main(_ARGS.parse_args())
