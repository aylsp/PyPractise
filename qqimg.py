# coding=utf-8

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

im = Image.open(r'C:\Users\Public\Pictures\Sample Pictures\flower.jpg')
# im.show()
w,h=im.size
print w,h
drawObject=ImageDraw.Draw(im)
Font1 = ImageFont.truetype("C:\Windows\Fonts\simsunb.ttf",120)
drawObject.text((w-80,1),"4",fill=128,font=Font1)
im.show()