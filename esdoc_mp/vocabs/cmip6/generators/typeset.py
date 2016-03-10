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

from esdoc_mp.ontologies.generators.python import utils
from esdoc_mp.vocabs.cmip6.core import VocabParser


# Define command line options.
_ARGS = argparse.ArgumentParser("Generates CMIP6 vocab typeset.")
_ARGS.add_argument(
    "--dest",
    help="Path to a directory into which vocab typeset defintions will be written.",
    dest="dest",
    type=str
    )



def _get_template():
    """Returns template to be generated.

    """
    loader = tornado.template.Loader(os.path.dirname(__file__))
    fname = __file__.split('/')[-1].replace('.py', '.tornado')

    return loader.load(fname)



class _VocabParser(VocabParser):
    def __init__(self):
        """Instance constructor.

        """
        super(_VocabParser, self).__init__()
        self.code = {}
        self.vocab = None
        self.template = _get_template()


    def on_vocab_parse(self, vocab):
        """On vocabulary parse event handler.

        """
        self.vocab = vocab


    def on_realm_parse(self, realm):
        """On realm parse event handler.

        """
        self.code[realm] = self.template.generate(r=realm, u=utils)


def _main(args):
    """Main entry point.

    """
    # Simply perform a vocab parse in order to create typeset.
    parser = _VocabParser()
    parser.parse()

    # Write typsets to file system.
    for realm, code in parser.code.items():
        fpath = os.path.join(args.dest, "{}.py".format(realm.id))
        with open(fpath, 'w') as f:
            f.write(code)


# Entry point.
if __name__ == '__main__':
    _main(_ARGS.parse_args())
