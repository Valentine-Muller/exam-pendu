import os
import sys
# import pygame


# Le chemin vers le dossier contenant les fichiers .py que l'on veut documenter.
sys.path.insert(0, os.path.abspath('../'))  # Remplacez '../' par le chemin approprié

# Configuration file for the Sphinx documentation builder.
project = 'exampendu'
copyright = '2024, valentine'
author = 'valentine'

# Extensions à utiliser
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    "sphinx_autodoc_typehints"
]

templates_path = ['_templates']
exclude_patterns = []

# Options pour la sortie HTML
napoleon_google_docstring = True
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
add_module_names = False
