import os
from filters import *
from additional_data import appendToDataframe

df_all = appendToDataframe(getData().to_frame())   # All tweets and strings from additional_data.py

def cleanData(df, info = True):
    #df = SpecialWordsFilter(df)
    if info: print("Lowering the text...")
    df = lowerPhrase(df)
    # if info: print("Removing symbols...")
    # df = symbolRemover(df)
    # return df
    if info: print("Removing emojies...")
    df = emojiRemover(df)
    # if info: print("Removing low frequent words...")
    # df = lowFrequentRemover(df)
    if info: print("Removing stop words...")
    df = stopWordsRemover(df)
    if info: print("Running extra filters...")
    df = df[df.Text != '']  # Empty lines
    df = df.apply(lambda x: x.str.strip()) # Spaces in start and end
    df['Text']=df['Text'].apply(lambda sentence: re.sub(' +', ' ', sentence)) # Multiple spaces between words
    df['Text']=df['Text'].apply(lambda sentence: " ".join([word for word in sentence.strip().split(" ") if len(word)!=1])) #words with one letter
    if info: print("Done!")
    return df.reset_index(drop = True)

df = cleanData(df_all)
# print(df.info())
print(df.head())
df.to_csv(f'{os.path.abspath(os.path.join(os.path.dirname(__file__),".."))}/Words/clean_data.csv', index=False)

df["Text"] = df["Text"].apply(lambda row: stem(row))
df.to_csv(f'{os.path.abspath(os.path.join(os.path.dirname(__file__),".."))}/Words/stemmed_final.csv')