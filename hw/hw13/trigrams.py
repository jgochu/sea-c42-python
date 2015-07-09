#!/usr/bin/env python
import random
import string

open_file = open('sherlock.txt', 'r')
text = open_file.read()

open_file.close()

#  remove unwanted characters
punc = string.punctuation
punc = punc.replace("'", "")  # keep apostropies
punc = punc.replace("-", "")  # keep hyphenated words

for char in ['\n', '--']:
    if char in text:
        text = text.replace(char, ' ')
for char in punc:
    if char in text:
        text = text.replace(char, '')

text = text.split()


trigrams = {}


def words(text):
    #  add words to dictionary in trigrams
    for(i, word) in enumerate(text):
        if i in range(len(text) - 2):
            trigrams.setdefault((text[i], text[i + 1]), []).append(text[i + 2])
    return trigrams


def text_builder(trigrams):

    new_text = []

    for i in range(30):
        new_sentence = list(random.choice(list(trigrams.keys())))
        for x in range(random.randint(3, 10)):
            additional_words = random.choice(list(trigrams.keys()))
            new_sentence.extend(additional_words)
        new_sentence[0] = new_sentence[0].capitalize()
        new_sentence[-1] += '.'
        new_text.extend(new_sentence)

    print(' '.join(new_text))

words(text)
text_builder(trigrams)
