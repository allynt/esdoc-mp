# -*- coding: utf-8 -*-

"""
.. module:: esdoc_mp.utils.runtime
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


def raise_error(msg, type=ESDOC_MP_Exception):
    """Helper function to raise a runtime error.

    :param msg: Error message.
    :type msg: str

    :param type: Error type.
    :type type: class

    """
    raise type(msg)


def throw(msg):
    """Throws an ES-DOC API error.

    :param msg: Error message.
    :type msg: str

    """
    raise_error(msg)


def log(msg):
    """Outputs a message to log.

    :param msg: Logging message.
    :type msg: str

    """
    print "ES-DOC MP :: " + str(msg)