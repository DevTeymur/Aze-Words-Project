import pandas as pd
import os


def GetFileNames():
    """This function returns csv files which in the same path. Return type list."""
    all_files = os.listdir()
    csv_files = []
    for file in all_files:
        if file.endswith('.csv'):
            csv_files.append(file)
    return csv_files


def MergeDataFrames(files_list):
    """This function concats dataframes."""
    main = pd.read_csv(files_list[0])
    for i in range(1, len(files_list)):
        df = pd.read_csv(files_list[i])
        main = pd.concat([main, df])
    return main


main = MergeDataFrames(GetFileNames())
