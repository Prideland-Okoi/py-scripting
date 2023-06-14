#!/usr/bin/python3
import os
# Add suffix to files in folder

for file in os.listdir('.'):
    if file.endswith('.txt'):
        old_file = os.path.join('.', file)
        new_file = os.path.join('.', os.path.splitext(file)[0] + '-cartoon' + os.path.splitext(file)[1])I
        os.rename(old_file, new_file)
