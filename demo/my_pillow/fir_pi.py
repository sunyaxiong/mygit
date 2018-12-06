#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image


im = Image.open("C:\Users\sunya\Desktop\img.jpg")
print im.format, im.size, im.mode
for i in dir(im):
    print i
print im.width, im.height
im.convert("L")
im.resize((1, 1))
im.save("a.PNG")
