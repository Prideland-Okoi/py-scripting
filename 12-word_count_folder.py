#!/usr/bin/python3
import os
# Count total words in each file of a folder

word_counts = {}
for file in os.listdir('.'):
    if file.endswith('.txt'):
        with open(file, 'r') as f:
            text = f.read()
            word_count = len(text.split())
            print(f'{file}:{word_count}')


# word_counts[file] = word_count
# sorted_files = sorted(word_counts.items(), key = lambda x : x[1])
# for file, word_count in sorted_files:
    # print(f'{file}:{word_count}')
