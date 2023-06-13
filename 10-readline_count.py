import os

file =os.path.join('.', 'vivo.txt')
with open(file, 'r') as f:
    lines = f.readlines()
    line_count = len(lines)

print(line_count)
