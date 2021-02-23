# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 11:26:26 2021

@author: szymo
"""

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

ps = PorterStemmer()

def process_word(word):
    word = ps.stem(word)
    word = word.lower()
    word = word.strip()
    return word

if __name__ == '__main__':
    categories = {}
    with open('categories_list_txt.txt', 'r') as params:
        for line in params.readlines():
            data = line
            cat, words = line[:line.find('; ')], line[line.find('; ') + 2:].split(', ')