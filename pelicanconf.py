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
         ('DSA 1', 'http://pilot.cs.virginia.edu/category/students'),
         ('COA 1', 'http://www.cs.virginia.edu/luther/COA1/'),
         ('DSA 2', 'http://pilot.cs.virginia.edu/category/students'),
         ('COA 2', 'http://www.cs.virginia.edu/luther/COA2/'),
         ('SDE', 'http://bit.ly/cs2501-sde-s19-info'),
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
    ('Courses', '/category/courses'),
    ('Info for Students', '/category/students'),
    ('Info for Incoming First Years', 'https://docs.google.com/document/d/1esOQQzBNSdaqjaaDFu3IZenMF8szbSURsP0aNKxRqXI/edit?usp=sharing'),
    ('Info for Faculty', '/category/faculty'),
    ('FAQ', '/category/faq')
)

SUMMARY_MAX_LENGTH = None

#ARTICLE_ORDER_BY = 'sortorder'
#PAGE_ORDER_BY = 'sortorder'
