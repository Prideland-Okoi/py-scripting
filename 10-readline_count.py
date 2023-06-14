#!/usr/bin/python3
import os
# Number of lines in a file


file = os.path.join('.', 'vivo.txt')
with open(file, 'r') as f:
    lines = f.readlines()
    line_count = len(lines)

print(line_count)
