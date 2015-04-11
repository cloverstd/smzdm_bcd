#!/usr/bin/env python
# encoding: utf-8

__author__ = 'Cloverstd'

import urllib2
import re

url = "http://www.smzdm.com/tag/" + urllib2.quote("白菜党")
headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36"
        }
request = urllib2.Request(url, headers=headers)
rv = urllib2.urlopen(request).read()

key = re.compile(ur'<h3 class="itemName"\><a href="(.*)" target="_blank">(.*)<span class="red"> (\d+)</span></a>')

rv = re.findall(key, rv)

item_tpl = """
<item uid="SMZDM" arg="{link}">
<title>{title}</title>
<subtitle>{subtitle}</subtitle>
<icon>smzdm.png</icon>
</item>
"""

print "<?xml version=\"1.0\"?><items>"
if rv:
    for item in rv:
        print item_tpl.format(link=item[0],
                              title=item[2],
                              subtitle=item[1]
                )

else:
    print item_tpl.format(link="",
                          title="出现了某些错误",
                          subtitle="获取失败"
            )


print "</items>"
