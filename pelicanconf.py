#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mollie Taylor'
SITENAME = u'Maps & Apps'
SITEURL = 'http://blog.mollietaylor.com'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

THEME = "pelican-themes/chunk"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('About Mollie', 'pages/about/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

TWITTER_USERNAME = "mollie_taylor"

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['better_code_samples', 'better_codeblock_line_numbering', 'feed_summary', 'pelican-gist']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
