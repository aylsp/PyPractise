# coding:utf-8


import os
import re
import urllib

os.path.join(r'/Users/xujianeng/', r'blog_spider')
os.mkdir(r'/Users/xujianeng/blog_spider')


def gethtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getimg(html):
    img_re = re.compile(r'src="(.+?\.jpg)"')
    imglist = re.findall(img_re, html)
    return imglist


blog_html = gethtml('http://canonxu.com/2014/11/Pycon2014@Shanghai/')
with open(r'/Users/xujianeng/blog_html.html', 'w') as f:
    f.write(blog_html)

blog_imglist = getimg(blog_html)
x = 0
for imgurl in blog_imglist:
    urllib.urlretrieve(imgurl, r'/Users/xujianeng/blog_spider/%s.jpg' % x)
    x += 1
