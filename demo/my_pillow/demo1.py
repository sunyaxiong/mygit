#!/usr/bin/env python
# -*- coding: utf-8 -*-
# "Python Image Library Test"
import os
import sys

from PIL import Image

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    print f, e
    outfile = f + ".png"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print("Cannot convert", infile)