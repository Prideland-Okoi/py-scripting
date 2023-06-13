#!/usr/bin/python3

import os

suffix = "-cartoon"
for file in os.listdir('.'):
    old_file = os.path.join('.', file)
    new_file = file.replace(suffix, '')
    os.rename(old_file, new_file)
