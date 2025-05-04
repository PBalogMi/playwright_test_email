import os
import sys
sys.path.insert(0, os.path.abspath('../'))  # Adjust the path to the root of your project


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'playwright_test_email'
copyright = '2025, Peter Balog'
author = 'PBalogMi'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'classic'
#html_theme = 'sphinx_rtd_theme'
#html_static_path = ['_static']
# Add sphinx_rtd_theme to extensions
extensions = [
    'sphinx_rtd_theme',
    'sphinx_copybutton',
    'sphinx.ext.autodoc',  # Add this line
    'sphinx.ext.viewcode',  # Optional: adds links to source code
    # ...any other extensions you may have...
]

html_baseurl = 'https://pbalogmi.github.io/playwright_test_email/'
