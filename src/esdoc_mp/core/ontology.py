# -*- coding: utf-8 -*-

"""
.. module:: esdoc_mp.core.ontology
   :platform: Unix, Windows
   :synopsis: Represents an ontology definition.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

# Module imports.
from operator import add
from functools import reduce

from esdoc_mp.core.class_ import Class
import esdoc_mp.utils.runtime as rt



class Ontology(object):
    """Represents an ontology, i.e. a set of classes organised into packages.

    :ivar name: Ontology name.
    :ivar version: Ontology version.
    :ivar doc_string: Ontology documentation string.
    :ivar packages: Set of associated packages.

    """

    def __init__(self, name, version, doc_string, packages):
        """Constructor.

        :param name: Ontology name.
        :type name: str
        
        :param version: Ontology version.
        :type version: str

        :param doc_string: Ontology documentation string.
        :type doc_string: str

        :param packages: Set of associated packages.
        :type packages: list

        """
        # Set relations.
        for pkg in packages:
            pkg.ontology = self

        # Set attributes.
        self.name = name
        self.version = version
        self.doc_string = doc_string
        self.packages = sorted(packages, key=lambda p: p.name)

        # Initialise output attributes.
        self.op_name = None
        self.op_version = None
        
        # Set supersets.
        self.classes = reduce(add, map(lambda p : p.classes, packages))
        self.decodings = reduce(add, map(lambda p : p.decodings, packages))
        self.enums = reduce(add, map(lambda p : p.enums, packages))
        self.enum_members = reduce(add, map(lambda e : e.members, self.enums), [])
        self.entities = reduce(add, map(lambda p : p.entities, packages))
        self.properties = reduce(add, map(lambda c : c.properties, self.classes))
        self.property_types = map(lambda p : p.type, self.properties)
        self.types = sorted(self.classes + self.enums)

        # Set base classes.
        _set_base_classes(self)
        
        # Set property type information.
        _set_property_type_info(self)

        # Set intra-class imports.
        _set_class_imports(self)

        # Set class circular imports.
        _set_circular_imports(self)

        # For each package assign packages used by it's classes.
        _set_associated_packages(self)
        

    def __repr__(self):
        """String representation for debugging."""
        return self.name + ' v' + self.version


    def get_type(self, name):
        """Returns type with matching name.

        :param name: Fully qualified name of target type.
        :type name: str

        """
        pkg_name = name.split('.')[0]
        type_name = name.split('.')[1]
        
        for t in self.types:
            if t.package.name == pkg_name and t.name == type_name:
                return t
            
        return None


def _set_base_classes(o):
    """Sets base classes."""
    for c in [c for c in o.classes if c.base is not None]:
        t = o.get_type(c.base)
        if t is not None:
            c.base = t
        else:
            msg = "Base class not found :: class = {0}.{1} :: base = {2}"
            msg = msg.format(c.package, c, c.base)
            rt.log(msg)


def _set_property_type_info(o):
    """Sets a property type flag indicating whether the property is related to an ontology class."""
    for pt in o.property_types:
        pt.cls = pt.package = None
        if pt.is_complex:
            t = o.get_type(pt.name)
            if t is not None:
                pt.is_class = isinstance(t, Class)
                pt.ontology = o
                pt.package = t.package
                pt.cls = t


def _set_class_imports(o):
    """Assigns set of intra-class imports."""
        # Set class imports.
    def append_to_class_imports(cls, pkg, type):
        if pkg != cls.package.name or \
           type != cls.name and \
           (pkg, type) not in cls.imports:
            cls.imports.append((pkg, type))

    for c in o.classes:
        if c.base is not None:
            append_to_class_imports(c, c.base.package.name, c.base.name)

        for p in [p for p in c.properties if p.type.is_complex]:
            append_to_class_imports(c, p.type.name_of_package, p.type.name_of_type)


def _set_circular_imports(o):
    """Assigns set of intra-class circular imports."""
    for c in o.classes:
        c_import = (c.package.name, c.name)
        for p in [p for p in c.properties if p.type.is_class]:
            p_type = o.get_type(p.type.name)
            if c_import in p_type.imports:
                p_type.imports.remove(c_import)
                p_type.circular_imports.append(c_import)


def _set_associated_packages(o):
    """Assigns set of intra-package classes."""
    def append(p, targets):
        for target in targets:
            if target != p and target not in p.associated:
                p.associated.append(target)

    for p in o.packages:
        # Packages associated with base classes.
        append(p, [c.base.package for c in p.classes if c.base is not None])
        for c in p.classes:
            # Packages associated with property types.
            for prp in c.properties:
                if prp.is_required and prp.type.package is not None:
                    append(p, [prp.type.package])
