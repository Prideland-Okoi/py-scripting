import os
file =os.path.join('.', 'vivo.txt')
word_counts = {}
with open(file, 'r') as f:
    text = f.read()
    word_count = len(text.split())
word_counts = word_count
print(word_counts)
