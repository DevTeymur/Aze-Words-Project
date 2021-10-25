import os
path = f'{os.path.abspath(os.path.join(os.path.dirname(__file__),".."))}/Words'


def stopwords(path=path):
    file=open(f'{path}/stopwords.txt', 'r')
    stopwords_list=[]
    for line in file.readlines():
        stopwords_list.append(line.rstrip('\n').lstrip('\ufeff'))
    return stopwords_list

def suffixes(path=path):
    file=open(f'{path}/suffix.txt', 'r')
    suffix_list=[]
    for line in file.readlines():
        suffix_list.append(line.strip('\n'))
    return suffix_list

def ReturnVocabulary(path=path):
    print('ReturnVocabulary call')
    file=open(f'{path}/words.txt', 'r')
    alphabet = ['a', 'b', 'c', 'ç', 'd', 'e', 'ə', 'f', 'g', 'ğ', 'h', 'x', 'ı', 'i', 'j', 'k', 'q',
                'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'y', 'z']
    vocabulary_dict={}
    for letter in alphabet:
        vocabulary_dict[letter]=[]

    for line in file.readlines():
        for letter in alphabet:
            if line.startswith(letter):
                vocabulary_dict[letter].append(line.rstrip('\n'))
    return vocabulary_dict
