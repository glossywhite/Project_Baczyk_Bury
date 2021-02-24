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
    for cat in categories.keys():
        cat_occurence[cat] = 0
        cat_positive = 0
        cat_negative = 0
        print(f'=== {cat.upper()} ===')
        for param in categories[cat].keys():
            param_occurence[param] = 0
            for token in in_txt_tokens_words:
                processed_word_params = process_word(param)
                processed_word_input = process_word(token)
                if processed_word_params == processed_word_input:
                    cat_occurence[cat] += 1
                    param_occurence[param] += 1
                    if categories[cat][param] == 'positive':
                        all_positive += 1
                        cat_positive += 1
                    else:
                        all_negative += 1
                        cat_negative += 1
                        
            print(f'"{param}" occurence: {param_occurence[param]}')
             
        print(f' >> {cat.upper()} occurence: {cat_occurence[cat]}')
        print(f' >> {cat.upper()} positives: {cat_positive}, negatives: {cat_negative}')
        
        cat_pos_neg = cat_positive + cat_negative
        if cat_positive != 0:
            print(f' >> {cat_positive / cat_pos_neg * 100}% of positives')
        if cat_negative != 0:
            print(f' >> {cat_negative / cat_pos_neg * 100}% of negatives')
        print('===============\n')
        
    print('\n\n')
    print('=== FINAL RESULTS ===')
    
    numbers = [cat_occurence[cat] for cat in cat_occurence]
    max = max(numbers)
    most_occured = [cat for cat in cat_occurence if cat_occurence[cat] == max]
    
    print('Mostly occuring:')
    for moc in most_occured_cat:
        print(f'{moc} occured {max} times')

























            