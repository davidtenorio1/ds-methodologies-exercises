import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
import wrangle
from sklearn.preprocessing import StandardScaler, QuantileTransformer, PowerTransformer, RobustScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

data = wrangle.wrangle_telco()
X = data.drop(columns='total_charges').set_index('customer_id')
y = data.total_charges


def split_my_data(X):
    train, test = train_test_split(X, train_size =.80, random_state = 123)
    return train, test


def standard_scaler(X):
    train, test =  split_my_data(X)
    scaler = StandardScaler(copy=True, with_mean=True, with_std=True).fit(train)
    train = pd.DataFrame(scaler.transform(train),columns=train.columns.values).set_index([train.index.values])
    test = pd.DataFrame(scaler.transform(test),columns=test.columns.values).set_index([test.index.values])
    return train, test, scaler


def scale_inverse(X):
    train, test, scaler = standard_scaler(X)
    train = pd.DataFrame(scaler.inverse_transform(train), columns = train.columns.values).set_index([train.index.values])
    test = pd.DataFrame(scaler.inverse_transform(test), columns = test.columns.values).set_index([test.index.values])
    return train, test


def uniform_scaler(X):
    train, test = split_my_data(X)
    scaler = QuantileTransformer(n_quantiles=100, output_distribution = 'uniform', random_state = 123, copy = True).fit(train)
    train = pd.DataFrame(scaler.transform(train), columns = train.columns.values).set_index([train.index.values])
    test = pd.DataFrame(scaler.transform(test),columns = test.columns.values).set_index([test.index.values])
    return train, test, scaler


def gaussian_scaler(X):
    train, test = split_my_data(X)
    scaler = PowerTransformer(method='yeo-johnson', standardize=False, copy=True).fit(train)
    train = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    test =  pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])
    return train, test, scaler

def min_max_scaler(X):
    train, test = split_my_data(X)
    scaler = MinMaxScaler(copy=True, feature_range=(0,1)).fit(train)
    train = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    test =  pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])
    return train, test, scaler


def iqr_robust_scaler(X):
    train, test = split_my_data(X)
    scaler = RobustScaler(quantile_range=(25.0,75.0), copy=True, with_centering=True, with_scaling=True).fit(train)
    train = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    test =  pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])
    return train, test, scaler







