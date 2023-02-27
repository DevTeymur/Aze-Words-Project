from file_reader import stopwords, suffixes, personNames, personSurnames
import pandas as pd
import pickle as pkl
import os
import re

path = f'{os.path.abspath(os.path.join(os.path.dirname(__file__),".."))}/Web_scraping/all.csv'

file = open(
    f'{os.path.abspath(os.path.join(os.path.dirname(__file__),".."))}/Words/Files/vocabulary.pkl', "rb")
vocabulary = pkl.load(file)
file.close()
suffix_list = suffixes()

def getData(path=path):
    df = pd.read_csv(path)
    df = df['Text']
    df = df.dropna()
    return df


def lowerPhrase(df):
    """
    Makes all letters lower case expect names and surnames
    """
    person_names_surnames = personNames() + personSurnames()
    df['Text'] = df['Text'].apply(lambda sentence: ' '.join(
        word if word in person_names_surnames else word.lower() for word in sentence.split()))
    
    # df['Text'] = df['Text'].str.lower()
    return df


def symbolRemover(df):
    """
    Removes symbols from text
    Problem here
    """
    df['Text'] = df['Text'].apply(lambda sentence: '    '.join(
        [word for word in sentence if word.isalnum() or word == ' ']))
    df['Text'] = df['Text'].str.replace('\d', '')
    return df


def stopWordsRemover(df):
    """
    Removes links, mentions, tags from the text
    """
    # df['Text'] = df['Text'].apply(lambda sentence: ' '.join([word for word in sentence.split() if word not in stopwords() and word.startswith('https') == False and
    #                                                          word.startswith('#') == False and word.startswith('@') == False]))
    df['Text'] = df['Text'].apply(lambda sentence: ' '.join([word for word in sentence.split() if word.startswith('http') == False and
                                                             word.startswith('#') == False and word.startswith('@') == False]))
    
    return df


def emojiRemover(df):
    """
    Removes emojies from the text
    """
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    for i in range(len(df['Text'])):
        df.iloc[i, :].Text = emoji_pattern.sub(
            r'', df.iloc[i, :].Text).strip('')
    return df


def lowFrequentRemover(df):
    """
    Removes words with low frequency
    """
    if df.shape[0] > 10000:
        words = pd.Series((' '.join(df['Text'].values)).split(
        )).value_counts().sort_values(ascending=False).tail(1000)
        df['Text'] = df['Text'].apply(lambda sentence: ' '.join(
            word for word in sentence.split() if word not in words))
    else:
        return df
    return df


def spellCheck():
    pass


def specialWordsFilter(df):
    """
    Removes special words
    """
    df['Text']=df['Text'].apply(lambda sentence: " ".join([word for word in sentence.strip().split(" ") if word.isupper()==False]))
    return df


def isInVocabulary(word, voc=vocabulary):
    """
    Searchs for word from dictonary based on first letter
    """
    first_letter = word[0]
    if first_letter not in voc:
        return False
    if word in voc[first_letter]:
        return True
    else:
        return False


def stemmer_old(df, s=sorted(suffix_list, key=len)[::-1]):
    """
    Loops all dataframe and returns processed strings
    """
    for index, sentence in enumerate(df['Text']):
        sentence = sentence.split()
        for word in sentence:  
            copy=word
            run=True
            if isInVocabulary(copy):
                continue 
            else:
                while run:
                    for i in range(len(s)):
                        if copy.endswith(s[i]):
                            copy=copy[::-1].replace(s[i][::-1], "", 1)[::-1]
                            break
                        elif copy.endswith(s[i]+'n') or copy.endswith(s[i]+'m') or copy.endswith(s[i]+'k') or copy.endswith(s[i]+'z'):
                            try:
                                if isInVocabulary(copy[:-3]):
                                    copy=copy[:-3]
                                    run=False 
                            except:
                                pass
                    if isInVocabulary(copy[:-1]+'q'):
                        copy=copy[:-1]+'q'
                        run=False
                    elif isInVocabulary(copy[:-1]+'k'):
                        copy=copy[:-1]+'k'
                        run=False
                    else:
                        for i in range(len(word), 0, -1):
                            if isInVocabulary(word[:i]):
                                sentence = [w.replace(word, word[:i]) for w in sentence]
                                break
                        run=False
            sentence = [w.replace(word, copy) for w in sentence]   
        df['Text'][index] = " ".join(sentence)
    return df



def stem(string):
    l=[]
    vowels=["a","ı","o","u","e","ə","i"]
    string=string.split()
    for i in string:
        if i.isupper() or (string.index(i)!=0 and i[0].isupper()):
            # xüsusi isimlər və abbr. üçün
            l.append(i)
        else:
            for j in range(len(i),0,-1):
                if isInVocabulary(i[:j].casefold()): # i[:j].casefold() in words:
                    # adi şəkilçilər üçün
                    l.append(i[:j])
                    break
                elif i[j-1] in vowels and (i[j-2]=="y" or i[j-2]=="ğ") :
                    # bitişdirici samitlər üçün
                    if isInVocabulary((i[:j-2]+"k").casefold()): # (i[:j-2]+"k").casefold() in words:
                        l.append(i[:j-2]+"k")
                        break
                    elif isInVocabulary((i[:j-2]+"q").casefold()): # (i[:j-2]+"q").casefold() in words:
                        l.append(i[:j-2]+"q")
                        break
    return ' '.join(l)