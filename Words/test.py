import pandas as pd
import numpy as np
from file_reader import suffixes

s=suffixes()

df=pd.DataFrame({'A': [1,2,3,4,5,6], 'B': [1,2,3,4,5,6], 'C': [1,2,3,4,5,6]})


df.loc[len(df)]=np.nan
df.loc[len(df)-1, 'B']='7'

word='kitablara'
for i in s:
    if word.endswith(i):
        word=word.replace(i, "")

print(word)