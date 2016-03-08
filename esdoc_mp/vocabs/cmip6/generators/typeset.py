# -*- coding: utf-8 -*-

"""
.. module:: write_cmip6_xmind.py
   :platform: Unix, Windows
   :synopsis: Rewrites cmip6 vocab defintions to xmind files.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import argparse
import os

import tornado

from esdoc_mp.vocabs.cmip6.core import VocabParser



# Define command line options.
_ARGS = argparse.ArgumentParser("Generates CMIP6 vocab typeset.")
_ARGS.add_argument(
    "--dest",
    help="Path to a directory into which vocab typeset defintions will be written.",
    dest="dest",
    type=str
    )


_TEMPLATE = __file__.replace('.py', '.tornado').split('/')[-1]

_TEMPLATE_LOADER = tornado.template.Loader(os.path.dirname(__file__))

print _TEMPLATE_LOADER.load(_TEMPLATE)





class _VocabParser(VocabParser):
    def __init__(self):
        """Instance constructor.

        """
        super(_VocabParser, self).__init__()
        self.code = None


    def on_vocab_parse(self, vocab):
        """On vocabulary parse event handler.

        """
        template = _TEMPLATE_LOADER.load(_TEMPLATE)
        self.code = template.generate(v=vocab)

        print self.code


def _main(args):
    """Main entry point.

    """
    # Simply perform a vocab parse in order to create typeset.
    parser = _VocabParser()
    parser.parse()

    # Write mindmaps to file system.
    # for domain, code in parser.code.items():
    #     fpath = os.path.join(args.dest, "{}.py".format(domain.id))
    #     with open(fpath, 'w') as f:
    #         f.write(code)


# Entry point.
if __name__ == '__main__':
    _main(_ARGS.parse_args())
