# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

sys.path.insert(0, os.path.abspath('..//..'))

project = 'Python, Playwright, BDD, Gherkin, Robot framework'
copyright = '2025, Peter'
author = 'Peter'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc",
              'sphinx_copybutton']

exclude_patterns = ['_build', 
                    'Thumbs.db', 
                    '.DS_Store'
                    ]

autodoc_default_options = {
    'members': True,  # Include only members by default
    'member_order': 'bysource',  # Order members by source code
    'exclude_members': '__init__',  # Exclude the __init__ method
    }

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

autodoc_docstring_signature = True

# [##From Python to Pytest BDD thanks to Playwright and Gherkin](https://pbalogmi.github.io/playwright_test_email/docs/index.html)
