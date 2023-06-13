#!/usr/bin/python3

import os

file = os.path.join('.', 'vivo.txt')
with open(file, 'w') as f:
    f.write('1. Keep the Beat\n2. My Own Drum\n3. One more Song')
