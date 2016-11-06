# coding:utf-8


import os
import re
import urllib.request

dir_name = os.path.join(r'F:\programming', r'blog_spider')
if not os.path.isdir(dir_name):
    os.mkdir(dir_name)


def gethtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


def getimg(html):
    img_re = re.compile(r'src="(.+?\.jpg)"')
    # html = html.encode('GBK')
    html=str(html, encoding="utf-8")
    imglist = re.findall(img_re, html)
    return imglist


blog_html = gethtml('http://canonxu.com/2014/11/Pycon2014@Shanghai/')
#with open(r'F:\programming\blog_html.html', 'w') as f:
f=open(r'F:\programming\blog_html.html', 'wb')
f.write(blog_html)
f.close()

blog_imglist = getimg(blog_html)
x = 0
for imgurl in blog_imglist:
    urllib.request.urlretrieve(imgurl, r'F:\programming\blog_spider\%s.jpg' % x)
    x += 1
