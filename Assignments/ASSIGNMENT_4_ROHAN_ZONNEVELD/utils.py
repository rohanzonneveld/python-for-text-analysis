import xml.etree.ElementTree as et

def load_root(path):
    """Find the root of an xml file given a filepath (str). """
    tree = et.parse(path)
    root = tree.getroot()
    return root

def get_talks(root):
    """Get all talk elements from an xml file."""
    talks = root.findall('file')
    return talks

def get_id(talk):
    """Get the id of a talk."""
    try:
        id = talk.find('head').find('talkid').text
    except:
        id = 'no id'

    return id

def get_date(talk):
    """Get the date of a talk."""
    try:
        date = talk.find('head').find('date').text
    except:
        date = 'no date'

    return date

def get_title(talk):
    """Get the title of a talk."""
    try:
        title = talk.find('head').find('title').text
    except:
        title = 'no title'

    return title

def get_speaker(talk):
    """Get the speaker of a talk."""
    try:
        speaker = talk.find('head').find('speaker').text
    except:
        speaker = 'no speaker'

    return speaker

def get_wc(talk):
    """Get the word count of a talk."""
    try:
        wc = talk.find('head').find('wordnum').text
    except:
        wc = 'no word count'

    return wc


