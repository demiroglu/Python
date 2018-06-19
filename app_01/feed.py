#!/usr/bin/env python
#-*-coding:utf-8-*-

import feedparser
d = feedparser.parse('https://www.ntv.com.tr/gundem.rss')
for post in d.entries:
    print (post.title.replace(u"\u2018", "'").replace(u"\u2019", "'") + ":\n" + post.summary.replace(u"\u2018", "'").replace(u"\u2019", "'")+"\n" + post.link + "\n\n")
