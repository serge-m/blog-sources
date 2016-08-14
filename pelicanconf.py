#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'sergem'
SITENAME = 'Personal public notebook'
SITEURL = ''

THEME='pelican-bootstrap3'

PATH = 'content'
USE_FOLDER_AS_CATEGORY = False

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

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
         # ('You can modify those links in your config file', '#'),
         )

# # Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


MAIN_MENU=True

DISPLAY_CATEGORIES_ON_SIDEBAR=True
RECENT_POST_COUNT=10
DISPLAY_RECENT_POSTS_ON_SIDEBAR=True
DISPLAY_TAGS_ON_SIDEBAR=True
DISPLAY_PAGES_ON_MENU=True