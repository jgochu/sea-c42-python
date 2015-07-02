#!/usr/bin/env python

open_file = open('sherlock-small.txt', 'r')
text = open_file.read()

open_file.close()

#  remove unwanted characters
text = text.replace('\n', ' ')
text = text.replace('--', ' ')
for char in ["\\", '(', ')', '-']:
    if char in text:
        text = text.replace(char, '')

text = text.split()

trigrams = {}

#  add words to dictionary in trigrams
for(i, word) in enumerate(text):
    if i in range(len(text) - 2):
        trigrams[(text[i], text[i + 1])] = [text[i + 2]]

print(trigrams)