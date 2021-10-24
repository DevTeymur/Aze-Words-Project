import os
path = f'{os.path.abspath(os.path.join(os.path.dirname(__file__),".."))}/Words'


def stopwords(path=path):
    f=open(f'{path}/stopwords.txt', 'r')
    stopwords=[]
    for line in f.readlines():
        stopwords.append(line.rstrip('\n').lstrip('\ufeff'))
    return stopwords