from lxml import etree as et
from utils import *

def find_wc(talks, length='longest'):
    """Find the talk with the minimum or maximum word count."""
    
    minmax_wc = None
    minmax_talk = None
    total_wc = 0
    for talk in talks:
        wc = int(get_wc(talk))
        total_wc += wc

        if minmax_wc == None:
            minmax_wc = wc
            minmax_talk = [talk]
        elif wc == minmax_wc:
            minmax_talk = [minmax_talk, talk]
        elif length == 'shortest' and wc < minmax_wc:
            minmax_wc = wc
            minmax_talk = [talk]
        elif length == 'longest' and wc > minmax_wc:
            minmax_wc = wc
            minmax_talk = [talk]
        
    title = []
    id = []  
    for talk in minmax_talk:
        title.append(get_title(talk))
        id.append(get_id(talk))
        wc = get_wc(talk)
    
    mean_wc = total_wc / len(talks)
    
    return title, id, int(wc), mean_wc

def find_date(talks, time='newest'):
    pass
    # return title, id

def find_speaker(talks):
    pass
    # return speaker_to_talks


def main():
    path = '/Users/rohanzonneveld/Documents/Artificial Intelligence/Jaar 2/Programming in Python for Text Analysis/python-for-text-analysis/Data/ted-talks/FILTERED_xml/ted_en.xml'
    root = load_root(path)
    talks = get_talks(root)
    test_talk = talks[0]
    print(find_wc(talks, length='longest'))



    
    # print(f'The total number of English talks is: [total number]\n')

    # print('Talk length:') 
    # print('Longest talk: [title] (id: [id])')
    # print('Shortest talk: [title] (id: [id])')
    # print('Mean word count: [mean word count]')


if __name__ == '__main__':
    main()