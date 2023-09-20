def preprocess(text, chars_to_remove={'\n', ',', '.', '"', '(', ')'}):
    '''
    * input: text (string), chars_to_remove (set)
    * output: text (string)

    This function takes a string and returns a string with all characters in chars_to_remove removed.
    '''
    for char in chars_to_remove:
        text = text.replace(char, '')
    return text
