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