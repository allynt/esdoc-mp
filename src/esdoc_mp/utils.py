# -*- coding: utf-8 -*-

"""
.. module:: esdoc_mp.utils
   :platform: Unix, Windows
   :synopsis: Runtime utilty functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

class ESDOC_MP_Exception(Exception):
    """Default library exception class.

    """

    def __init__(self, message):
        """Contructor.

        :param message: Exception message.
        :type message: str

        """
        self.message = str(message)


    def __str__(self):
        """Returns a string representation.

        """
        return "ES-DOC MP :: !!! EXCEPTION !!! : {0}".format(repr(self.message))


def raise_error(msg, type_=ESDOC_MP_Exception):
    """Helper function to raise a runtime error.

    :param str msg: Error message.
    :type msg: str

    :param class type: Error type.

    """
    raise type_(msg)


def log(msg):
    """Outputs a message to log.

    :param msg: Logging message.
    :type msg: str

    """
    if msg.startswith('-'):
        print(msg)
    else:
        print("ES-DOC Meta-Programming Framework :: {}".format(msg))