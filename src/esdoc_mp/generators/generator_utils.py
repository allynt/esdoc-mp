"""
.. module:: esdoc_mp.generators.generator_utils
   :platform: Unix, Windows
   :synopsis: Set of common generator utility functions.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""

# Module imports.
import datetime
import os
import pwd



# Templates folder.
_TEMPLATE_FOLDER = os.path.dirname(__file__)

# Standard 4 character python indent.
_INDENT = '    '

# Standard line return.
_LINE_RETURN = '\n'

# Set of loaded templates.
_loaded_templates = dict()


def convert_to_camel_case(name, separator='_'):
    """Converts passed name to camel case.

    :param name: A name as specified in ontology specification.
    :param separator: Separator to use in order to split name into constituent parts.
    :type name: str
    :type separator: str

    """
    r = ''
    if name is not None:
        s = name.split(separator)
        for s in s:
            if (len(s) > 0):
                r += s[0].upper()
                if (len(s) > 1):
                    r += s[1:]
    return r


def convert_to_pascal_case(name, separator='_'):
    """Converts passed name to camel case.

    :param name: A name as specified in ontology specification.
    :param separator: Separator to use in order to split name into constituent parts.
    :type name: str
    :type separator: str

    """
    r = ''
    s = convert_to_camel_case(name, separator)
    if (len(s) > 0):
        r += s[0].lower()
        if (len(s) > 1):
            r += s[1:]
    return r


def _load_template(language, filename):
    """Returns code template.

    :param language: Generator language.
    :type language: str

    :param filename: Name of template file.
    :type filename: str

    """
    path = _TEMPLATE_FOLDER + "/{0}/templates/{1}".format(language, filename)
           
    if path not in _loaded_templates:
        tmpl = open(path)
        _loaded_templates[path] = tmpl.read()
        tmpl.close()
        
    return _loaded_templates[path]


def load_templates(language, filenames):
    """Returns a dictionary of loaded code templates.

    :param language: Generator language.
    :type language: str

    :param filenames: Set of template file names.
    :type filenames: iterable

    """
    templates = {}
    for filename in filenames:
        templates[filename] = _load_template(language, filename)

    return templates


def get_username():
    """Returns name of current user.

    """
    try:
        return pwd.getpwuid(os.getuid()).pw_name
    except ImportError:
        return os.environ.get("USERNAME")


def emit_indent(count=1):
    """Emits code corresponding to a code indentation.

    :param count: Number of indentations to emit.
    :type count: int

    """
    return reduce(lambda x, y: x + _INDENT, range(count), '')


def emit_line_return(count=1):
    """Emits code corresponding to a code line return.

    :param count: Number of line returns to emit.
    :type count: int

    """
    return reduce(lambda x, y: x + _LINE_RETURN, range(count), '')


def create_directory(dir):
    """Generates a directory into which code will be generated.

    :param dir: Target code generation directory.
    :type dir: str

    """
    try:
        os.makedirs(dir)
    except:
        pass


def write_file(code, dir, file):
    """Writes code to a file.

    :param code: Code to be written to a file.
    :param dir: Directory into which code is to be generated.
    :param file: Name of code file being written.
    :type code: str
    :type dir: str
    :type file: str

    """
    # Create directory.
    create_directory(dir)

    # Update code.
    code = code.replace('{file-name}', file)

    # Write file.
    file = open(dir + "/" + file, 'w')
    file.writelines(code)
    file.close()


def format_code(ctx, code):
    """Formats code prior to being written to file system.

    :param ctx: Generation context information.
    :type ctx: esdoc_mp.generators.generator.GeneratorContext
    
    :param code: Code to be injected with standard params.
    :type code: str
    
    """
    # Ontology related params.
    code = code.replace('{ontology-name}', ctx.ontology.op_name)
    code = code.replace('{ontology-version}', ctx.ontology.op_version)
    code = code.replace('{ontology-version-packagename}', ctx.ontology.op_version.replace('.', '_'))

    # Misceallaneous params.
    code = code.replace('{datetime-now}', str(datetime.datetime.now()))
    code = code.replace('{datetime-year}', str(datetime.datetime.now().year))
    code = code.replace('{user-name}', get_username())

    return code
