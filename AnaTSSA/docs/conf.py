# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import subprocess
import inspect
sys.path.insert(0, os.path.abspath("../src/python/"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Transverse Single Spin Assymetry Study for SpinQuest'
copyright = '2024, Chatura Kuruppu, Ph.D'
author = 'Chatura Kuruppu, Ph.D.'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc'              ,
              'sphinx.ext.autosectionlabel'     ,
              'sphinx.ext.autosummary'          ,
              'sphinx.ext.coverage'             ,
              'sphinx.ext.doctest'              ,
              'sphinx.ext.duration'             ,
              'sphinx.ext.extlinks'             ,
              'sphinx.ext.githubpages'          ,
              'sphinx.ext.graphviz'             ,
              'sphinx.ext.ifconfig'             ,
              'sphinx.ext.imgconverter'         ,
              'sphinx.ext.inheritance_diagram'  ,
              'sphinx.ext.intersphinx'          ,
              #'sphinx.ext.linkcode'             ,
              'sphinx.ext.napoleon'             ,
              'sphinx.ext.todo'                 ,
              'sphinx.ext.viewcode'

                ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_show_sphinx = False