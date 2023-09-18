import os
import sys
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter

def get_paths(input_folder):
    '''
    * takes one positional parameter called *input_folder*
    * the function stores all paths to .txt files in the *input_folder* in a list
    * the function returns a list of strings, i.e., each string is a file path
    '''
    paths = os.listdir(input_folder)
    with open('paths.txt', 'w') as f:
        for path in paths:
            f.write(path + '\n')
    return paths

def get_basic_stats(txt_path):
    '''
    * takes one positional parameter called *txt_path*
    * the function returns a dictionary with the following key-value pairs:
        * 'num_sents': number of sentences in the text
        * 'num_tokens': number of tokens in the text
        * 'vocab_size': number of unique tokens in the text
        * 'num_chapters': number of chapters in the text
        * 'top_30_tokens': a list of tuples, where each tuple contains a token and its frequency
    '''
    
    text = open(txt_path, 'r').read()
    num_sents = len(sent_tokenize(text))
    num_tokens = len(word_tokenize(text))
    vocab_size = len(set(word_tokenize(text)))
    if txt_path.endswith('AnnaKarenina.txt'):
        num_chapters_or_acts = text.count('Chapter ')
    elif txt_path.endswith('HuckFinn.txt'):
        num_chapters_or_acts = text.count('CHAPTER')
    elif txt_path.endswith('Macbeth.txt'):
        num_chapters_or_acts = text.count('ACT')
    else:
        sys.exit('Error: unknown book')

    counter = Counter(word_tokenize(text))
    top_30_tokens = counter.most_common(30)
    
    return {'num_sents': num_sents, 'num_tokens': num_tokens, 'vocab': vocab_size, 'num_chapters': num_chapters_or_acts, 'top_30_tokens': top_30_tokens}