#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Thomas Antony'
SITENAME = 'Thomas Antony'
SITEURL = ''
SITESUBTITLE = 'Academic CV'

PATH = 'content'

TIMEZONE = 'America/Indiana/Indianapolis'

DEFAULT_LANG = 'en'

THEME='themes/pelican-clean-blog'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Social widget
SOCIAL = (('twitter', 'http://www.twitter.com/thomasantony'),
          ('linkedin', 'http://www.linkedin.com/in/thomasantony'),
          ('github', 'https://github.com/thomasantony'),)

TWITTER_URL = SOCIAL[0][1]
FACEBOOK_URL = SOCIAL[1][1]
GITHUB_URL = SOCIAL[2][1]
SHOW_SOCIAL_ON_INDEX_PAGE_HEADER = True

DEFAULT_PAGINATION = False

STATIC_PATHS = ['static']

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DIRECT_TEMPLATES = ('publications', )

# Plugins
PLUGIN_PATHS = ['plugins/']
PLUGINS = ['pelican-bibtex']
PUBLICATIONS_SRC = 'content/pubs.bib'
