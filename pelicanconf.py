#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Chiayo Lin'
SITENAME = u'chiayolin.org'
SITEURL = 'http://chiayolin.org'

PATH = 'content'
STATIC_PATHS = ['etc/CNAME']
EXTRA_PATH_METADATA = {'etc/CNAME': {'path': 'CNAME'},}

THEME = 'lowlands'

TIMEZONE = 'Asia/Taipei'
DEFAULT_DATE_FORMAT = '%a %b %d %Y'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
