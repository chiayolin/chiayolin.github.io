#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from markdown.extensions.codehilite import CodeHiliteExtension
# from markdown.extensions.toc import TocExtension

# site meta
AUTHOR = u'Chiayo Lin'
SITENAME = u'chiayolin.org'
SITEURL = ''

# import theme
THEME = './lowlands'

# paths
PATH = 'content'
STATIC_PATHS = [
    'etc/CNAME', 
    'etc/favicon.ico']
EXTRA_PATH_METADATA = {
    'etc/CNAME': {'path': 'CNAME'}, 
    'etc/favicon.ico': {'path': 'favicon.ico'}} 

# urls and generated path
ARTICLE_URL = 'posts/{slug}/'
ARTICLE_SAVE_AS = 'a/{date:%y}{date:%m}{date:%d}{date:%k}.html'
ARCHIVES_SAVE_AS = 'a/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = '{slug}.html'

# i don't need these
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS =''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''

# time and date
TIMEZONE = 'Asia/Taipei'
DEFAULT_DATE_FORMAT = '%a %b %d %Y'

# local language
DEFAULT_LANG = u'en'

# import markdown extenstions
MD_EXTENSIONS = [
    CodeHiliteExtension(css_class='highlight'),
    'markdown.extensions.extra',
    # TocExtension(permalink=True),
]

# disable pagenation
DEFAULT_PAGINATION = False
