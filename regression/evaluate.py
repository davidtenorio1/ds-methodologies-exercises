import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
from pydataset import data
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.linear_model import LinearRegression
from statsmodels.formula.api import ols

df = data("tips")
df['x'] = df['total_bill']
df['y'] = df['tip']
x = pd.DataFrame(df['x'])
y = pd.DataFrame(df['y'])
ols_model = ols('y ~ x', data=df).fit()
df['yhat'] = ols_model.predict(x)
yhat = pd.DataFrame(df['yhat'])


def plot_residuals(x, y, dataframe):
    sns.set(style="whitegrid")
    return sns.residplot(x, y, color="b")

def regression_errors(y, yhat):
    SSE = mean_squared_error(df.y, df.yhat)*len(df)
    ESS = sum((df.yhat - df.y.mean())**2)
    TSS = ESS + SSE
    MSE = SSE/len(df)
    RMSE = sqrt(MSE)
    return SSE, ESS, TSS, MSE, RMSE










