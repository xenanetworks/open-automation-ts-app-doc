# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../../'))

# import pkg_resources

import codecs
import os.path

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

def get_short_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__short_version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

# -- Project information -----------------------------------------------------

project = u'Xena OpenAutomation Test Suite Application User Documentation'
copyright = u'2023, Xena Networks'
author = u'Xena Networks'
title = u'Xena OpenAutomation Test Suite Application User Documentation'

# The full version, including alpha/beta/rc tags.
release = "1.0.0"

# The short X.Y version.
version = "1.0"


# -- General configuration -----------------------------------------------------

# A boolean that decides whether module names are prepended to all object names 
# (for object types where a “module” of some kind is defined), e.g. for py:function directives. 
add_module_names = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.extlinks',
    "sphinx_inline_tabs",
    'sphinx_copybutton',
    "sphinx_remove_toctrees",
]

# The default options for autodoc directives. 
# They are applied to all autodoc directives automatically. 
# It must be a dictionary which maps option names to the values.
autodoc_default_options = {
    'member-order': 'bysource',
    'private-members': False,
    'undoc-members': False,
    'show-inheritance': True
}
autodoc_typehints = 'signature'
autodoc_typehints_format = 'short'
autodoc_inherit_docstrings = True

autosectionlabel_prefix_document = True

# The suffix(es) of source filenames.
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# These patterns also affect html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The master toctree document.
master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Enable numref
numfig = True

# -- Options for HTML output -----------------------------------------------------

# The theme to use for HTML and HTML Help pages.
html_theme = 'furo'

# Output file base name for HTML help builder.
htmlhelp_basename = 'xoa_app_doc'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = title

# The path to the HTML logo image in the static path, or URL to the logo, or ''.
# html_logo = './_static/xoa_logo.png'

html_favicon = './_static/xoa_favicon_16.png'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# If true, “(C) Copyright …” is shown in the HTML footer.
html_show_copyright = True

# If true, “Created using Sphinx” is shown in the HTML footer
html_show_sphinx = False

html_theme_options = {
    "light_logo": "xoa_logo_light.png",
    "dark_logo": "xoa_logo_dark.png",
    "source_repository": "https://github.com/xenanetworks/open-automation-python-api",
    "light_css_variables": {
        "color-brand-primary": "#295341",
        "color-brand-content": "#295341",
    },
    "navigation_with_keys": True,
}

# If true, the index is generated twice: once as a single page with all the entries, 
# and once as one page per starting letter. Default is False.
html_split_index = False


# -- Options for Texinfo output -----------------------------------------------------

# This config value contains the locations and names of other projects that should be linked to in this documentation.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

intersphinx_disabled_domains = ['std']

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'xoa_app_doc', title, author, 'xoa_app_doc', 'Xena Networks Documentation.', 'Miscellaneous'),
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']


# -- Options for LaTeX output -----------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
'papersize': 'a4paper',

# The font size ('10pt', '11pt' or '12pt').
'pointsize': '12pt',

# Additional stuff for the LaTeX preamble.
#'preamble': r'',

# Latex figure (float) alignment
#'figure_align': 'htbp',

#'printindex': r'\def\twocolumn[#1]{#1}\printindex',
'makeindex': r'\usepackage[columns=1]{idxlayout}\makeindex',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [(master_doc, 'xoa_app_doc.tex', title, author, 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = './_static/pdf_logo.png'

# -- Options for manual page output -----------------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'xoa_app_doc', title, [author], 1)
]


# -- Options for EPUB output -----------------------------------------------------
epub_title = title + ' ' + release
epub_author = author
epub_publisher = 'https://xenanetworks.com'
epub_copyright = copyright
epub_show_urls = 'footnote'
epub_basename = 'xoa_app_doc'
