import pandas as pd
import os
import numpy as np
import datetime

path = os.path.dirname(os.path.abspath(__file__))+'/Data'

def getFileNames(print_file_names=False):
    """This function returns csv files which in the same path. Return type list."""
    all_files = os.listdir(path)
    csv_files = []
    for file in all_files:
        if file.endswith('.csv'):
            csv_files.append(file)
    if print_file_names:
        print(csv_files)
    return csv_files


def mergeDataFrames(files_list):
    """This function concats dataframes."""
    main = pd.read_csv(f'{path}/{files_list[0]}')
    for i in range(1, len(files_list)):
        df = pd.read_csv(f'{path}/{files_list[i]}')
        main = pd.concat([main, df])
    return main

def txtToFrame(file_name, scname, url, show_data=False):
    table={'Id': [], 'Screen_name': [], 'Created_at': [], 'Text': [], 'Url': [], 'Hastags': [], 'Symbols': []}
    f= open(f'{path}/{file_name}.txt', 'r') 
    for line in f:
        if line.rstrip()!="":
            table['Id'].append(np.nan)
            table['Screen_name'].append(scname)
            table['Created_at'].append(datetime.datetime.now())
            table['Text'].append(line.rstrip())
            table['Url'].append(url)
            table['Hastags'].append(np.nan)
            table['Symbols'].append(np.nan)
    data=pd.DataFrame(table)
    if show_data:
        print(data.head(10))
        print(data.shape)
    return data
    
    

main = mergeDataFrames(getFileNames())
main = pd.concat([main, txtToFrame('data', 'oxu.az', 'oxu.az')], ignore_index=True)
print(main.shape)

main.to_csv(f'{os.path.dirname(os.path.abspath(__file__))}/all.csv', index=False)


