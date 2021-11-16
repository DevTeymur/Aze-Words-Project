from test_cases import AppendToDataframe, string_list
from file_reader import stopwords, suffixes
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

def GetData(path=path):
    df = pd.read_csv(path)
    df = df['Text']
    return df


def LowerPhrase(df):
    df['Text'] = df['Text'].apply(lambda sentence: ' '.join(
        word.lower() for word in sentence.split()))
    return df


def SymbolRemover(df):
    df['Text'] = df['Text'].apply(lambda sentence: ''.join(
        [word for word in sentence if word.isalnum() or word == ' ']))
    df['Text'] = df['Text'].str.replace('\d', '')
    return df


def StopWordsRemover(df):
    df['Text'] = df['Text'].apply(lambda sentence: ' '.join([word for word in sentence.split() if word not in stopwords() and word.startswith('https') == False and
                                                             word.startswith('#') == False and word.startswith('@') == False]))
    return df


def EmojiRemover(df):
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


def LowFrequentRemover(df):
    if df.shape[0] > 10000:
        words = pd.Series((' '.join(df['Text'].values)).split(
        )).value_counts().sort_values(ascending=False).tail(1000)
        df['Text'] = df['Text'].apply(lambda sentence: ' '.join(
            word for word in sentence.split() if word not in words))
    else:
        return df
    return df


def SpellCheck():
    pass


def SpecialWordsFilter(df):
    df['Text']=df['Text'].apply(lambda sentence: " ".join([word for word in sentence.strip().split(" ") if word.isupper()==False]))
    return df


def Search(word, voc=vocabulary):
    first_letter = word[0]
    if first_letter not in voc:
        return False
    if word in voc[first_letter]:
        return True
    else:
        return False


def Lemmatizer(df, s=sorted(suffix_list, key=len)[::-1]):
    for index, sentence in enumerate(df['Text']):
        sentence = sentence.split()
        for word in sentence:  
            copy=word
            run=True
            if Search(copy):
                continue 
            else:
                while run:
                    for i in range(len(s)):
                        if copy.endswith(s[i]):
                            copy=copy[::-1].replace(s[i][::-1], "", 1)[::-1]
                            break
                        elif copy.endswith(s[i]+'n') or copy.endswith(s[i]+'m') or copy.endswith(s[i]+'k') or copy.endswith(s[i]+'z'):
                            if Search(copy[:-3]):
                                copy=copy[:-3]
                                run=False 
                    if Search(copy[:-1]+'q'):
                        copy=copy[:-1]+'q'
                        run=False
                    elif Search(copy[:-1]+'k'):
                        copy=copy[:-1]+'k'
                        run=False
                    else:
                        for i in range(len(word), 0, -1):
                            if Search(word[:i]):
                                sentence = [w.replace(word, word[:i]) for w in sentence]
                                break
                        run=False
            sentence = [w.replace(word, copy) for w in sentence]   
        df['Text'][index] = " ".join(sentence)
    return df


def CleanData(df):
    df = SpecialWordsFilter(df)
    df = LowerPhrase(df)
    df = SymbolRemover(df)
    df = EmojiRemover(df)
    df = LowFrequentRemover(df)
    df = StopWordsRemover(df)
    df = df[df.Text != '']  # Empty lines
    df = df.apply(lambda x: x.str.strip()) # Spaces in start and end
    df['Text']=df['Text'].apply(lambda sentence: re.sub(' +', ' ', sentence)) # Multiple spaces between words
    df['Text']=df['Text'].apply(lambda sentence: " ".join([word for word in sentence.strip().split(" ") if len(word)!=1])) #words with one letter
    return df
    
