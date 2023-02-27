import os
import pickle as pkl
path = f'{os.path.abspath(os.path.join(os.path.dirname(__file__),".."))}/Words/Files'

def stopwords(path=path):
    """
    Returns list of stopwords
    """
    file=open(f'{path}/stopwords.txt', 'r')
    stopwords_list=[]
    for line in file.readlines():
        stopwords_list.append(line.rstrip('\n').lstrip('\ufeff'))
    file.close()
    return stopwords_list

def suffixes(path=path):
    """
    Retruns list of suffixes
    """
    file=open(f'{path}/suffix.txt', 'r')
    suffix_list=[]
    for line in file.readlines():
        suffix_list.append(line.strip('\n'))
    file.close()
    return suffix_list

def returnVocabulary(path=path):
    """
    Returns vocabulary of dictonary
    Keys: letters of alphabet
    Values: list of correspondig words
    """
    file=open(f'{path}/words.txt', 'r')
    alphabet=['a', 'b', 'c', 'ç', 'd', 'e', 'ə', 'f', 'g', 'ğ', 'h', 'x', 'ı', 'i', 'j', 'k', 'q',
                'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'y', 'z']
    vocabulary_dict={}
    for letter in alphabet:
        vocabulary_dict[letter]=[]

    for line in file.readlines():
        for letter in alphabet:
            if line.startswith(letter):
                vocabulary_dict[letter].append(line.rstrip('\n'))
    file.close()
    return vocabulary_dict

def personNames(path=path):
    """
    Returns list of valid person names
    """
    f = open(f'{path}/names_raw.txt','r')

    valid_names = []
    for line in f.readlines():
        if len(line) >= 3:
            valid_names.append(line.replace('\n', ''))

    f.close()
    return valid_names

def personSurnames(path=path):
    """
    Returns list of valid person surnames
    """
    f = open(f'{path}/surnames_raw.txt','r')

    valid_surnames_men = []
    for line in f.readlines():
        if len(line) >= 3:
            valid_surnames_men.append(line.replace('\n', ''))

    f.close()

    valid_surnames_women = [element + 'a' for element in valid_surnames_men]

    all_surnames = valid_surnames_men + valid_surnames_women
    return all_surnames

# One time call in order to create and save vocabulary to use for efficient search
'''
vocabulary=returnVocabulary()
file=open(f"{path}/vocabulary.pkl","wb")
pkl.dump(vocabulary, file)
file.close()
'''