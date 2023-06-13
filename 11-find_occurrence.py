import os
import re
from collections import Counter

file = os.path.join('.', 'vivo.txt')

with open(file, 'r') as f:
    text = f.read()
    # Add lower() func to avoid double count
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    for word, count in word_counts.items():
        print(f'{word}: {count}')

