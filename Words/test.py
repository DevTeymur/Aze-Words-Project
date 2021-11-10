from functools import partial
import re
import pandas as pd
import numpy as np
from file_reader import suffixes
from filter import Search

s=sorted(suffixes(), key=len)[::-1]

df=pd.DataFrame({'A': [1,2,3,4,5,6], 'B': [1,2,3,4,5,6], 'C': [1,2,3,4,5,6]})


df.loc[len(df)]=np.nan
df.loc[len(df)-1, 'B']='7'

word='torpağı' 
word1='kitablara'


a=word
run=True
if Search(a):
    print('Yes')
else:
    while run:
        for i in range(len(s)):
            if a.endswith(s[i]):
                print(s[i])
                a=a[::-1].replace(s[i][::-1], "", 1)[::-1]
                print(a)
                break
            
        if Search(a):
            run=False
            break
        else:
            break

print(word)
print(a)
