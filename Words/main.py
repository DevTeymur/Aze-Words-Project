from filter import CleanData, GetData
from test_cases import AppendToDataframe
import os


df_all = AppendToDataframe(GetData().to_frame())
df = CleanData(df_all)

df.to_csv(
    f'{os.path.abspath(os.path.join(os.path.dirname(__file__),".."))}/Words/result.csv', index=False)
