import os
import sys
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter

def get_paths(input_folder):
    '''
    * input: input_folder (string)
    * output: paths (list of strings)

    * This function stores all paths to files in the input folder
        in a new .txt file (paths.txt) in the input_folder
        It also returns a list of all paths
    '''
    paths = os.listdir(input_folder)
    out_path = os.path.join(input_folder, 'paths.txt')
    with open(out_path, 'w') as f:
        f.write('\n'.join(paths))
    
    return paths

def get_basic_stats(txt_path):
    '''
    * input: txt_path (string)
    * output: a dictionary with the following key-value pairs:
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