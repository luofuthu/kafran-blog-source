#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Site Settings
AUTHOR = u'Kolmar Kafran'
SITENAME = u'kafran.net'
SITEURL = 'http://localhost:8000'

# Regional Settings
TIMEZONE = 'America/Recife'
DATE_FORMATS = {
    'en': ('en_US','%B %d, %Y'),
    'pt': ('pt_BR','%d de %b de %Y'),
}
DEFAULT_LANG = u'en'

# Plugins and extensions
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc(permalink=true)']
PLUGIN_PATH = '../pelican-plugins/'
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search', 'liquid_tags.img']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.8,
        'indexes': 0.6,
        'pages': 0.4
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Appearance
TYPOGRIFY = True
THEME = '../pelican-themes/pelican-elegant'
DEFAULT_PAGINATION = False

# Defaults
DEFAULT_CATEGORY = 'Outros'
USE_FOLDER_AS_CATEGORY = True
PAGE_URL = u'{slug}.html'
PAGE_SAVE_AS = u'{slug}.html'
PAGE_LANG_URL = u'{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = u'{slug}-{lang}.html'
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
DEFAULT_DATE = 'fs'

# Feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Social widget
SOCIAL = (
		('Twitter', 'http://twitter.com/doutorchefe'),
        ('Github', 'http://github.com/kafran'),
        ('Email', '&#x6d;ai&#108;&#116;o&#58;bl&#x6f;g&#64;&#107;a&#102;&#114;&#x61;&#110;.n&#101;t'),
        )

# Elegant theme
RECENT_ARTICLES_COUNT = 7
COMMENTS_INTRO = u'So what do you think? Did I miss something? Is any part unclear? Leave your comments below.'
SITE_LICENSE = u'<span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">kafran.net</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://kafran.net" property="cc:attributionName" rel="cc:attributionURL">Kolmar Kafran</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.'
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
SITE_DESCRIPTION = u'My name is Kolmar Kafran. I am kafran at Github and @doutorchefe at twitter. I am a Brazilian federal employee that have a passion for technologies and management. This is my personal blog.'
# PROJECTS = [
#        {
#            'name': 'Elegant',
#            'url':
#            'http://oncrashreboot.com/pelican-elegant',
#            'description': 'A clean and distraction free Pelican theme, with'
#            ' search and a'
#            ' lot more unique features. Built with Jinja2 and Bootstrap'},
#			]
LANDING_PAGE_ABOUT = {'title': 'Wellcome to my personal blog',
        'details': """<div itemscope itemtype="http://schema.org/Person"><p>My name
        is <span itemprop="name">Kolmar Kafran</span>.
       I am <a href="https://github.com/talha131/" title="My Github
       profile" itemprop="url"><span itemprop="nickname">kafran</span></a> at Github and <a
       href="https://twitter.com/doutorchefe/" title="My Twitter
       profile" itemprop="url">@doutorchefe</a> at twitter. You can also reach me via <a
       href="&#x6d;ai&#108;&#116;o&#58;bl&#x6f;g&#64;&#107;a&#102;&#114;&#x61;&#110;.n&#101;t" title="My email
       address" itemprop="email">email</a>.</p><p>I work on <a href="http://www.ifpb.edu.br/"
       title="IFPB" itemprop="affiliation">IFPB</a> which is a Brazilian federal college.</p><p>I have a passion for technologies and management. I'm trying to learn web technologies like HTML5, CSS and javascript.</p><p>I try to<a
       href="http://runkeeper.com/user/kafran/profile" title="My
       runkeeper profile" itemprop="url">exercise</a> and <a
       href="http://www.goodreads.com/" title="My GoodReads profile" itemprop="url">read books</a> regularly. To be a stronger and better version of
       myself!</p><p>English is my second language.""" }
STATIC_PATHS = ['theme/img', 'img']
SOCIAL_PROFILE_LABEL = u'Stay in Touch'
CUSTOM_CSS = True
USE_FAVICON = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
