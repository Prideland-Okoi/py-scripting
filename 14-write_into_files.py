#!/usr/bin/python3
import os

for files in os.listdir('.'):
    if files.endswith('.html'):
        with open(files, 'w') as f:
            f.write('{% extends "base.html" %}')
