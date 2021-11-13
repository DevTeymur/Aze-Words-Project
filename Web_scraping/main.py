import pandas as pd
import os

path = os.path.dirname(os.path.abspath(__file__))+'/Data'

def GetFileNames(print_file_names=False):
    """This function returns csv files which in the same path. Return type list."""
    all_files = os.listdir(path)
    csv_files = []
    for file in all_files:
        if file.endswith('.csv'):
            csv_files.append(file)
    if print_file_names:
        print(csv_files)
    return csv_files


def MergeDataFrames(files_list):
    """This function concats dataframes."""
    main = pd.read_csv(f'{path}/{files_list[0]}')
    for i in range(1, len(files_list)):
        df = pd.read_csv(f'{path}/{files_list[i]}')
        main = pd.concat([main, df])
    return main


main = MergeDataFrames(GetFileNames(True))
print(main.shape)

main.to_csv('all.csv', index=False)

