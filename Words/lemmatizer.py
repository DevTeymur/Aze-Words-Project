import pandas as pd
from filter import Lemmatizer
import os

df = pd.read_csv(f'{os.path.abspath(os.path.join(os.path.dirname(__file__),".."))}/Words/result.csv')
df= Lemmatizer(df)
df.to_csv(f'{os.path.abspath(os.path.join(os.path.dirname(__file__),".."))}/Words/final.csv')


