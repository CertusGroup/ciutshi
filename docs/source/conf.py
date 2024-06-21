# pylint: disable=C0103,W0622,C0114,C0301
# flake8: noqa
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import datetime
# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'ciuTshi'
copyright = f'{datetime.datetime.now().year} Certus Core. All rights reserved'
author = "<a href='https://www.certuscore.com' target='_blank'>Certus Core</a>"

# The full version, including alpha/beta/rc tags
release = '0.2.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
        'myst_parser',
]

# MyST-Parser Configuration
myst_footnote_transition = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store', '.env']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'
html_theme_options = {
    "repository_url": "https://github.com/CertusGroup/ciutshi",
    "use_repository_button": True,
    "use_issues_button": True,
    "primary_sidebar_end": ["certus_core"],
}
html_title = "the Adaptable Data Operations Standard"
html_logo = "static/images/ciutshi_logo.png"
html_favicon = "static/images/favicon.png"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['static']
