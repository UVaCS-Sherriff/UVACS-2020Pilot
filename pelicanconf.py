#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Mark Sherriff'
SITENAME = 'UVA CS - 2020 Curriculum Pilot'
SITEURL = 'http://pilot.cs.virginia.edu'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
         ('Courses', '#'),
         ('Piazza', '#')
)

# Social widget
#SOCIAL = (('Twitter', 'http://twitter.com/marksherriff'),
#          ('Github', 'http://github.com/marksherriff'),)

DEFAULT_PAGINATION = None

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'pelican-bootstrap3'

BOOTSTRAP_THEME = 'flatly'

DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = (
    ('Apply to Join', '#'),
    ('Courses', '#'),
    ('Info for Students', '#'),
    ('Info for Faculty', '#')
    ('FAQ', '#')
)

SUMMARY_MAX_LENGTH = None

#ARTICLE_ORDER_BY = 'sortorder'
#PAGE_ORDER_BY = 'sortorder'