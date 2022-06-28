import pandas as pd
from filter import lemmatizer
import os

df = pd.read_csv(f'{os.path.abspath(os.path.join(os.path.dirname(__file__),".."))}/Words/result.csv')
df= lemmatizer(df)
df.to_csv(f'{os.path.abspath(os.path.join(os.path.dirname(__file__),".."))}/Words/final.csv')
