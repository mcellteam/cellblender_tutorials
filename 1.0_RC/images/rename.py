#!/usr/bin/env python

import os

files = os.listdir(os.getcwd())

for f in files:
    if f.endswith("png"):
        os.system("mv %s sc_sm_%s" % (f, f))
