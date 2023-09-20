import os
from utils import *

def map_languages_to_path(folder_path:str):
    '''
    * input: path to folder with xml files
    * output: dict mapping languages to paths of xml files
    '''
    # create empty dict
    languages_to_path = {}

    # loop over all files in folder
    for file in os.listdir(folder_path):
        # get language from filename and remove .xml
        language = file.split('_')[1][:-4]
        # add language and path to dict
        languages_to_path[language] = folder_path + '/' + file
    
    return languages_to_path

def find_coverage(languages_to_path:dict, n_languages:str):
    '''
    * input:    dict mapping languages to paths of xml files
                most/least translations ("most"/"least")
    * output:   dict mapping languages to coverage

    This function finds the language(s) with the most/least translations.
    '''
    # initialize empty dict
    language_to_coverage = {}
    # initialize minmax variables
    minmax_coverage = None
    minmax_language = None

    # loop over all languages
    for language in languages_to_path.keys():
        # skip english since this is the source language
        if language == 'en':
            continue
        # extract talks from xml file
        path = languages_to_path[language]
        root = load_root(path)
        talks = get_talks(root)
        
        # calculate coverage
        coverage = len(talks)
        # update minmax variables
        if minmax_coverage == None:
            minmax_coverage = coverage
            minmax_language = [language]
        elif coverage == minmax_coverage:
            minmax_language.append(language)
        elif n_languages == 'most' and coverage > minmax_coverage:
            minmax_coverage = coverage
            minmax_language = [language]
        elif n_languages == 'least' and coverage < minmax_coverage:
            minmax_coverage = coverage
            minmax_language = [language]

    # add minmax variables to dict    
    for language in minmax_language:
        language_to_coverage[language] = minmax_coverage 

  
    return language_to_coverage

def get_id_title_dict(en_file_path):
    '''
    * input: path to english xml file
    * output: dict mapping ids to titles

    This function creates a dict mapping talk ids to talk titles.
    '''
    # initialize empty dict
    id_title_dict = {}
    # extract talks from xml file
    root = load_root(en_file_path)
    talks = get_talks(root)
    # loop over all talks
    for talk in talks:
        # add id and title to dict
        id = get_id(talk)
        title = get_title(talk)
        id_title_dict[id] = title
    
    return id_title_dict

def map_talks_to_languages(languages_to_path):
    '''
    * input: dict mapping languages to paths of xml files
    * output: dict mapping talk id to languages that talk is translated into
    
    This function creates a dict mapping talk ids to the languages that talk is translated into.
    '''
    # initialize empty dict
    id_to_languages = {}
    # loop over all languages
    for language in languages_to_path.keys():
        # skip english since this is the source language
        if language == 'en':
            continue
        # extract talks from xml file
        path = languages_to_path[language]
        root = load_root(path)
        talks = get_talks(root)
        # loop over all talks
        for talk in talks:
            id = get_id(talk)
            # create new key if id is not in dict yet
            if id not in id_to_languages.keys():
                id_to_languages[id] = [language]
            # add language to list of languages if id is already in dict
            else:
                id_to_languages[id].append(language)
    
    return id_to_languages

def map_nlang_to_talks(id_to_languages):
    '''
    * input: dict mapping talk id to languages that talk is translated into
    * output: dict mapping amount of languages talks are translated into to their corresponding talk ids

    This function creates a dict mapping the amount of languages talks are translated into to their corresponding talk ids.
    '''
    # initialize empty dict
    nlang_to_talks = {}
    # loop over all talkIDs
    for id in id_to_languages.keys():
        # get amount of languages that talk is translated into
        n_languages = len(id_to_languages[id])
        # create new key if n_languages is not in dict yet
        if n_languages not in nlang_to_talks.keys():
            nlang_to_talks[n_languages] = [id]
        # add talkID to list of talkIDs if n_languages is already in dict
        else:
            nlang_to_talks[n_languages].append(id)
    
    return nlang_to_talks

def find_top_coverage(languages_to_path, n_languages):
    '''
    * input:    dict mapping languages to paths of xml files
                most/least translations ("most"/"least")
    * output:   dict mapping most/least translated talks to their corresponding languages

    This function finds the most/least translated talks and maps them to their corresponding languages.
    '''
    # create dict mapping talk ids to languages that talk is translated into
    id_to_languages = map_talks_to_languages(languages_to_path)
    # create dict mapping amount of languages talks are translated into to their corresponding talk ids
    nlang_to_talks = map_nlang_to_talks(id_to_languages)

    # find most/least translated talks
    if n_languages == 'most':
        n_languages = max(nlang_to_talks.keys())
    elif n_languages == 'least':
        n_languages = min(nlang_to_talks.keys())

    # create dict mapping talk id to talk title
    id_to_title = get_id_title_dict(languages_to_path['en'])

    # get the ids of the most/least translated talks
    ids = nlang_to_talks[n_languages]
    # create empty dict
    talks_to_languages = {}
    # loop over all ids
    for id in ids:
        # create dict mapping talk title to languages that talk is translated into
        # use try/except to skip talks that are not in the english xml file
        try:
            title = id_to_title[id]
            talks_to_languages[title] = id_to_languages[id]
        except:
            pass
    
    return talks_to_languages

def main():
    languages_to_path = map_languages_to_path('..Data/ted-talks/FILTERED_xml')
    
    language_to_coverage = find_coverage(languages_to_path, 'most')
    language, translations = list(language_to_coverage.items())[0]
    print(f'\nThe language with the most translations is: {language} with {translations} translations\n')

    language_to_coverage = find_coverage(languages_to_path, 'least')
    language, translations = list(language_to_coverage.keys()), list(language_to_coverage.values())
    print(f'The language(s) with the least translations is/are: {language} with {translations[0]} translation(s)\n')

    talks_to_languages = find_top_coverage(languages_to_path, 'most')
    id_title_dict = get_id_title_dict(languages_to_path['en'])

    for title, languages in talks_to_languages.items():
        # find id by searching for the title as value
        id = next((key for key, value in id_title_dict.items() if value == title), None)
        print(f'The talk "{title}" (talkID: {id}) is translated into {len(languages)} languages: {languages}\n')

def test():
    languages_to_path = map_languages_to_path('..Data/ted-talks/FILTERED_xml')
    id_to_languages = map_talks_to_languages(languages_to_path)
    print(id_to_languages)

if __name__ == '__main__':
    main()
    # test()