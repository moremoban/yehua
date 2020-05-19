# -*- coding: utf-8 -*-
DESCRIPTION = (
    'Yet another a project template tool for an organisation.' +
    ''
)
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
spelling_word_list_filename = 'spelling_wordlist.txt'
project = u'yehua'
copyright = u'2017-2020 Onni Software Ltd.'
version = '0.1.0'
release = '0.1.0'
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
