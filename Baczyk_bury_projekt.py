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
            
            dict_words = {}
            for word in words:
                w = word.split(':')
                dict_words[w[0]] = w[1].replace('\n', '')
            categories[cat] = dict_words
            
    with open('test_text_input.txt', 'r') as input_text:
        in_txt = input_text.read()

    in_txt_tokens_words = word_tokenize(in_txt)
    
    all_positive = 0
    all_negative = 0
    cat_occurence = {}
    param_occurence = {}