#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Mark Sherriff'
SITENAME = 'UVA CS 2020 Curriculum Pilot'
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
         ('DSA 1', '#'),
         ('COA 1', '#'),
         ('CS 2020 Piazza', 'https://piazza.com/class/jf2oe8mypdf3mk'),
         ('Email for Questions', 'mailto:cs2020pilot-questions@virginia.edu')
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
    ('Apply to Join', 'https://goo.gl/forms/GP1FkCng6Zd2vMC73'),
    ('Courses', '/category/courses'),
    ('Info for Students', '/category/students'),
    ('Info for Faculty', '/category/faculty'),
    ('FAQ', '/category/faq')
)

SUMMARY_MAX_LENGTH = None

#ARTICLE_ORDER_BY = 'sortorder'
#PAGE_ORDER_BY = 'sortorder'