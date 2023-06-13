#!/usr/bin/python3

import os

for filename in os.listdir('.'):
    if filename.endswith('.txt'):
        print(filename)
