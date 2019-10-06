# -*- coding: utf-8 -*-
DESCRIPTION = (
    'An interactive command line tool to provide a default scaffolding for ' +
    'a python package.' +
    ''
)
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinxcontrib.spelling'
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
spelling_word_list_filename = 'spelling_wordlist.txt'
project = u'yehua'
copyright = u'2017-2019 Onni Software Ltd.'
version = '0.0.7'
release = '0.0.7'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'yehuadoc'
latex_elements = {}
latex_documents = [
    ('index', 'yehua.tex',
     'yehua Documentation',
     'Onni Software Ltd.', 'manual'),
]
man_pages = [
    ('index', 'yehua',
     'yehua Documentation',
     [u'Onni Software Ltd.'], 1)
]
texinfo_documents = [
    ('index', 'yehua',
     'yehua Documentation',
     'Onni Software Ltd.', 'yehua',
     DESCRIPTION,
     'Miscellaneous'),
]
