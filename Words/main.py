from filter import cleanData, getData
from test_cases import appendToDataframe
import os


df_all = appendToDataframe(getData().to_frame())
df = cleanData(df_all)

df.to_csv(
    f'{os.path.abspath(os.path.join(os.path.dirname(__file__),".."))}/Words/result.csv', index=False)
