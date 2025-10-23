import pandas as pd
import numpy as np

data_imputation = {
    'Experience (Years)': [2, 5, np.nan, 3, 6, np.nan, 7],
    'Salary': [35000, 60000, 75000, np.nan, np.nan, 55000, 80000]
    }

df= pd.DataFrame(data_imputation)

df_mean = df.fillna(df.mean())
df_median = df.fillna(df.median())
df_mode = df.fillna(df.mode().iloc[2])

print("MEAN \n", df_mean)
print("MEDIAN \n",  df_median)
print("MODE \n", df_mode)