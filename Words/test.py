# import pandas as pd
# import numpy as np
# from file_reader import suffixes
# from filter import Search
# import os

# s=sorted(suffixes(), key=len)[::-1]

# df=pd.DataFrame({'A': [1,2,3,4,5,6], 'B': [1,2,3,4,5,6], 'C': [1,2,3,4,5,6]})

# path = f'{os.path.abspath(os.path.join(os.path.dirname(__file__),".."))}/Web_scraping/Data'

# d = {'Text': []}

# for i in range(10):
#     d['Text'].append(i)

# import pandas as pd
# print(pd.DataFrame(data=d).head())


import os

def personSurnames(path= f'{os.path.abspath(os.path.join(os.path.dirname(__file__),".."))}/Words/Files'):
    f = open(f'{path}/surnames_raw.txt','r')

    valid_surnames_men = []
    for line in f.readlines():
        if len(line) >= 3:
            valid_surnames_men.append(line.replace('\n', ''))

    f.close()

    valid_surnames_women = [element + 'a' for element in valid_surnames_men]

    all_surnames = valid_surnames_men + valid_surnames_women
    return all_surnames

print(personSurnames())
'''
df.loc[len(df)]=np.nan
df.loc[len(df)-1, 'B']='7'

word1='torpağı' 
word2='düşdün'
word='kitablara'
print(word1[:-3])

a=word
run=True
if Search(a):
    print(word)
else:
    while run:
        for i in range(len(s)):
            if a.endswith(s[i]):
                print(s[i])
                a=a[::-1].replace(s[i][::-1], "", 1)[::-1]
                print(a)
                break
            elif a.endswith(s[i]+'n')or a.endswith(s[i]+'m') or a.endswith(s[i]+'k') or a.endswith(s[i]+'z'):
                if Search(a[:-3]):
                    a=a[:-3]
                    run=False
            
        if Search(a):
            run=False
            break
        else:
            if Search(a[:-1]+'q'):
                a=a[:-1]+'q'
                run=False
            elif Search(a[:-1]+'k'):
                a=a[:-1]+'k'
                run=False

print(word)
print(a)
'''

