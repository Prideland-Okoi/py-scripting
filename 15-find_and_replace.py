#!/usr/bin/python3
import os
search_text = 'base'
replace_text = 'main/base'

for files in os.listdir('.'):
    if files.endswith('.html'):
        with open(files, 'r+') as f:
            data = f.read()
        data = data.replace(search_text, replace_text)
        with open(files, 'w') as f:
            f.write(data)
