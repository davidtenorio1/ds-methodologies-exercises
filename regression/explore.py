import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
import wrangle, split_scale
from sklearn.preprocessing import StandardScaler, QuantileTransformer, PowerTransformer, RobustScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

data = wrangle.wrangle_telco()
X = data.drop(columns='total_charges').set_index('customer_id')
y = data.total_charges
scaler = StandardScaler().fit(data)


def plot_variable_pairs(dataframe):
    return

def months_to_years(tenure_months, df):
    df['tenure_years'] = (tenure_months/12).round()
    return df
