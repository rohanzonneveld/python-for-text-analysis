from lxml import etree as et
from utils import *

def find_wc(talks, length='longest'):
    """
    * input:    list of talks (positional)
                length of talk ("longest"/"shortest")
    * output:   title, id, word count, mean word count of the longest/shortest talk
    
    Find the talk with the minimum or maximum word count.
    """
    
    
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

    minmax_date = None
    minmax_talk = None

    for talk in talks:
        date = get_date(talk)
        if minmax_date == None:
            minmax_date = date
            minmax_talk = [talk]
        elif date == minmax_date:
            minmax_talk = [minmax_talk, talk]
        elif time == 'oldest' and date < minmax_date:
            minmax_date = date
            minmax_talk = [talk]
        elif time == 'newest' and date > minmax_date:
            minmax_date = date
            minmax_talk = [talk]
    
    title = []
    id = []
    for talk in minmax_talk:
        title.append(get_title(talk))
        id.append(get_id(talk))
    
    return title, id

def find_speaker(talks):
    '''
    * input: list of talk elemenets (position)
    * output: dict mapping speakers with more than one talk to their talks (tuple of talk title and id)
    '''

    speaker_to_talks = {}
    for talk in talks:
        speaker = get_speaker(talk)
        if speaker not in speaker_to_talks.keys():
            speaker_to_talks[speaker] = [(get_title(talk), get_id(talk))]
        else:
            speaker_to_talks[speaker].append((get_title(talk), get_id(talk)))
    
    # delete all speakers with only one talk
    for speaker in list(speaker_to_talks.keys()):
        if len(speaker_to_talks[speaker]) == 1:
            del speaker_to_talks[speaker]
    
    return speaker_to_talks


def main():
    path = '..Data/ted-talks/FILTERED_xml/ted_en.xml'
    # path = '../Data/ted-talks/XML_releases/xml/ted_en-20160408.xml'
    
    root = load_root(path)
    talks = get_talks(root)

    title, id, wc, mean_wc = find_wc(talks, length='longest')
    print(f'\nThe longest talk is: {title[0]} (id: {id[0]}, word count: {wc})')
    title, id, wc, mean_wc = find_wc(talks, length='shortest')
    print(f'The shortest talk is: {title[0]} (id: {id[0]}, word count: {wc})')
    print(f'The average word count is: {mean_wc}\n')

    title, id = find_date(talks, time='oldest')
    print(f'The oldest talk is: {title[0]} (id: {id[0]})')
    title, id = find_date(talks, time='newest')
    print(f'The newest talk is: {title[1]} (id: {id[1]})\n')

    speaker_to_talks = find_speaker(talks)
    k = 3
    print(f'Speakers with more than one talk: {list(speaker_to_talks.keys())[:k]} (truncated at {k} speakers, total: {len(speaker_to_talks.keys())})\n')

    print(f'The total number of English talks is: {len(talks)}\n')


if __name__ == '__main__':
    main()