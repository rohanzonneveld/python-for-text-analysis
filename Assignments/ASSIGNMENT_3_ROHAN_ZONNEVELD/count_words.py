from utils_3a import preprocess

def my_word_count(text):
    '''
    * input: text (string)
    * output: word_freq (dictionary)

    This function takes a string and returns a dictionary with the words as keys and the number of times each word appears as values.
    '''
    
    text = preprocess(text)
    words = text.split()

    word_freq = {}
    for word in words:
        if word not in word_freq:
            word_freq[word] = 1
        else:
            word_freq[word] += 1
    return word_freq

def main():
    '''
    This function tests the preprocess and my_word_count function.
    '''

    text = 'this is a (tricky) test'
    print(f'\nOriginal text: {text}')
    print(f'Preprocessed text: {preprocess(text, chars_to_remove={"(", ")"})}')

    text = 'this is a (very very very very tricky) test. This is another tricky test'
    print(f'\nOriginal text: {text}')
    print(f'Word count: {my_word_count(text)}')

if __name__ == '__main__':
    main()