#!/usr/bin/python3

import os

for file in os.listdir('.'):
    old_name = file
    new_name = 'movies-' + file
    if file.endswith('txt'):
        os.rename(old_name, new_name)
