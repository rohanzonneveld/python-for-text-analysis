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
    id = talk.find('head').find('talkid').text
    return id

def get_date(talk):
    """Get the date of a talk."""
    date = talk.find('head').find('date').text
    return date

def get_title(talk):
    """Get the title of a talk."""
    title = talk.find('head').find('title').text
    return title

def get_speaker(talk):
    """Get the speaker of a talk."""
    speaker = talk.find('head').find('speaker').text
    return speaker

def get_wc(talk):
    """Get the word count of a talk."""
    wc = talk.find('head').find('wordnum').text
    return wc
