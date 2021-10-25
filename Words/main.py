from test_cases import AppendToDataframe
from file_reader import stopwords, ReturnVocabulary, suffixes
import pandas as pd
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
    df['Text']=df['Text'].apply(lambda sentence: ' '.join([word for word in sentence.split() if word not in stopwords() and word.startswith('https')==False]))
    return df

def LowFrequentRemover(df):
    if df.shape[0]>10000:
        words=pd.Series((' '.join(df['Text'].values)).split()).value_counts().sort_values(ascending=False).tail(1000)
        df['Text']=df['Text'].apply(lambda sentence: ' '.join(word for word in sentence.split() if word not in words))
    else:
        pass
    return df

def SpellCheck():
    pass 

def SpecialWordsFilter():
    #df['Text']=df['Text'].apply(lambda sentence: " ".join([word for word in sentence.strip().split(" ") if not re.match(r"[A-Z]",word)]))
    pass

def Lemmatizer():
    pass



df=GetData().to_frame()
df=AppendToDataframe(df)
df=LowerPhrase(df)
df=SymbolRemover(df)
df=StopWordsRemover(df)
df=LowFrequentRemover(df)




