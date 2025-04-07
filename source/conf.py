# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '蔡子诺'
copyright = '2025, Zinuo Cai'
author = 'Zinuo Cai'
release = ''

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_permalinks_icon = '<span>#</span>'
html_theme = 'sphinxawesome_theme'

globaltoc_collapse = True
html_last_updated_fmt = '%Y-%m-%d %H:%M'
html_static_path = ['_static']

html_sidebars = {
   '**': ['globaltoc.html'],
}

html_title = ''

from docutils.parsers.rst import roles
from docutils import nodes

def setup(app):
    app.add_css_file('custom.css')  # 添加自定义CSS文件
    roles.register_local_role('blue', blue_role)

def blue_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    return [nodes.inline(rawtext, text, classes=['blue'])], []
