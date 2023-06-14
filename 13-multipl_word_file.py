#!/usr/bin/python3
import os
import re
from collections import Counter

"Count words in multiple files at once in a folder"

word_counts = Counter()
for file in os.listdir('.'):
    if file.endswith('.txt'):
        filename = os.path.join('.', file)
        with open(filename, 'r') as f:
            text = f.read()
            words = re.findall(r'\b\w+\b', text.lower())
            word_counts.update(words)
            for word, count in word_counts.items():
                print(f'{word}:{count}')
