"""
.. module:: esdoc_mp.ontologies.core.__init__.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: esdoc_mp.ontologies.core package initializer.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from esdoc_mp.ontologies.core.class_ import Class
from esdoc_mp.ontologies.core.class_constraint import ClassConstraint
from esdoc_mp.ontologies.core.class_pstr import ClassPrintString
from esdoc_mp.ontologies.core.computed_property import ComputedProperty
from esdoc_mp.ontologies.core.decoding import Decoding
from esdoc_mp.ontologies.core.enum import Enum
from esdoc_mp.ontologies.core.enum_member import EnumMember
from esdoc_mp.ontologies.core.ontology import Ontology
from esdoc_mp.ontologies.core.package import Package
from esdoc_mp.ontologies.core.property import Property
from esdoc_mp.ontologies.core.type_ import Type
from esdoc_mp.ontologies.core.factory import create_ontology
