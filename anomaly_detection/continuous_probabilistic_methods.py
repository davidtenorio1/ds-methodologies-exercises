import pandas as pd
import numpy as np 

df = pd.read_csv('lemonade.csv')
df.shape

def get_lower_and_upper_bounds(df):
    ratio = 1.5
    q1 = df.quantile(0.25)
    q3 = df.quantile(0.75)
    iqr = q3 - q1
    lower_limit = q1 - (ratio*iqr)
    upper_limit = q3 + (ratio*iqr)
    return lower_limit, upper_limit

get_lower_and_upper_bounds(df)