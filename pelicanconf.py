#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Antonio Luppi'
SITENAME = "Antonio Luppi's Blog"
SITEURL = 'antonioluppi.github.io/'

PATH = 'content'
THEME = "../pelican-themes/medius"
THEME_STATIC_DIR= 'output/theme'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Tarrafa Hacker Clube', 'http://tarrafa.net'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Linkedin', 'https://br.linkedin.com/in/antonioluppi'),
          ('GitHub', 'https://github.com/antonioluppi'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
