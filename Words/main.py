import test_cases as tc
from file_reader import stopwords
import pandas as pd
import re
import os
path = f'{os.path.abspath(os.path.join(os.path.dirname(__file__),".."))}/Web_scraping/all.csv'

def GetData(path=path):
    df=pd.read_csv(path)
    df=df['Text']
    return df

def LowerPhrase(df):
    df['Text']=df['Text'].apply(lambda sentence: ' '.join(word.lower() for word in sentence.split()))
    return df

def SymbolRemover(df):
    df['Text']=df['Text'].apply(lambda sentence: ''.join([word for word in sentence if word.isalnum() or word==' ']))
    df['Text']=df['Text'].str.replace('\d', '')
    return df

def StopWordsRemover(df):
    df['Text']=df['Text'].apply(lambda sentence: ' '.join([word for word in sentence.split() if word not in stopwords()]))
    return df

def LowFrequentRemover():
    pass

def SpecialWordsFilter():
    #df['Text']=df['Text'].apply(lambda sentence: " ".join([word for word in sentence.strip().split(" ") if not re.match(r"[A-Z]",word)]))
    pass

def Lemmatizer():
    pass

df=GetData().to_frame()
df=LowerPhrase(df)
df=SymbolRemover(df)
df=StopWordsRemover(df)
print(df)

    


