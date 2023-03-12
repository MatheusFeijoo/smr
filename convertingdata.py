import pandas as pd
import numpy as np

df = pd.read_csv('dataresult.csv', sep=',')
df = df.replace(np.nan,0)
pd.options.display.float_format = '{:,.0f}'.format
print(df)


