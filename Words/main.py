import test_cases as tc
import pandas as pd
import os
path = f'{os.path.abspath(os.path.join(os.path.dirname(__file__),".."))}/Web_scraping/all.csv'

def GetData(path=path):
    df=pd.read_csv(path)
    df=df['Text']
    return df

print(GetData())

def SymbolRemover():
    pass

def StopWordsRemover():
    pass

def LowFrequentRemover():
    pass

def Lemmatizer():
    pass

'''
f = open("words.txt", "r",  encoding="utf8")
words = f.readlines()

str1 = "".join(words)
words = str1.split("\n")

# moterze reqemler tire olkeler adlar seherler


def empty(i):
    if i != "" and i != "," and i != ":" and i != "\"":
        return True
    else:
        return False
 

def check(test):
    l = []
    vowels = ["a", "ı", "o", "u", "e", "ə", "i"]
    test = test.split()
    print(test)
    for i in test:
        if i.isupper() or (test.index(i) != 0 and i[0].isupper()):
            # xüsusi isimlər və abbr. üçün
            l.append(i)
            print(i)
        else:
            for j in range(len(i), 0, -1):
                if i[:j].casefold() in words:
                    print(i[:j])
                    # adi şəkilçilər üçün
                    #l.append( "".join(   i[0:].split(i[:j]) )  )
                    l.append(i[:j])
                    break
                elif i[j-1] in vowels and (i[j-2] == "y" or i[j-2] == "ğ"):
                    # bitişdirici samitlər üçün
                    if (i[:j-2]+"k").casefold() in words:
                        print(i[:j-2]+"k")
                        l.append(i[:j-2]+"k")
                        break
                    elif (i[:j-2]+"q").casefold() in words:
                        print(i[:j-2]+"q")
                        l.append(i[:j-2]+"q")
                        break

    # print(l)
    # return set(filter(empty,l))
    return l


check(tc.test5)
'''