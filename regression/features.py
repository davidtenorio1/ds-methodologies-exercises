# Our scenario continues:
# As a customer analyst, I want to know who has spent the most money with us over their lifetime. 
# I have monthly charges and tenure, so I think I will be able to use those two attributes as features to estimate total_charges. 
# I need to do this within an average of $5.00 per customer.

import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
import statsmodels.api as sm
import wrangle
import split_scale
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import SelectKBest, f_regression
from statsmodels.formula.api import ols
from sklearn.linear_model import LassoCV
import warnings
from sklearn.feature_selection import RFE
warnings.filterwarnings("ignore")

data = wrangle.wrangle_telco()
X = data.drop(columns='total_charges').set_index('customer_id')
y = pd.DataFrame(data.total_charges).set_index(data['customer_id'])
y_train, y_test = split_scale.split_my_data(y)
X_train, X_test = split_scale.split_my_data(X)



# 1.) Write a function, select_kbest_freg() that takes X_train, y_train and k as input (X_train and y_train should not be scaled!) and returns a list of the top k features.
def select_kbest_freg_unscaled(X_train, y_train, k):
    f_selector = SelectKBest(f_regression, k=k).fit(X_train, y_train)
    f_support = f_selector.get_support()
    f_feature = X_train.loc[:,f_support].columns.tolist()
    return (str(len(f_feature)), 'selected features'),(f_feature),(f_selector.scores_)



# 2.) Write a function, select_kbest_freg() that takes X_train, y_train (scaled) and k as input and returns a list of the top k features.


def select_kbest_freg_scaled(X_train, y_train, k):
    X_train_scaled, X_test_scaled, X_scaler = split_scale.min_max_scaler(X_train)
    y_train_scaled, y_test_scaled, y_scaler = split_scale.min_max_scaler(y_train)
    f_selector = SelectKBest(f_regression, k=k).fit(X_train_scaled, y_train_scaled)
    f_support = f_selector.get_support()
    f_feature = X_train.loc[:,f_support].columns.tolist()
    return (str(len(f_feature)), 'selected features'),(f_feature),(f_selector.scores_)



# 3.) Write a function, ols_backward_elimination() that takes X_train and y_train (scaled) as input and returns selected features based on the ols backwards elimination method.

def ols_backward_elimination(X_train, y_train):
    X_train_scaled, X_test_scaled, X_scaler = split_scale.min_max_scaler(X_train)
    y_train_scaled, y_test_scaled, y_scaler = split_scale.min_max_scaler(y_train)
    cols = list(X_train_scaled.columns)
    pmax = 1
    while (len(cols) > 0):
        p = []
        x_1 = X_train_scaled[cols]
        model = sm.OLS(y_train_scaled, x_1).fit()
        p = pd.Series(model.pvalues.values[0:,],index=cols)
        pmax = max(p)
        feature_with_pmax = p.idxmax()
        if(pmax>0.05):
            cols.remove(feature_with_pmax)
        else:
            break
    return cols



# 4.) Write a function, lasso_cv_coef() that takes X_train and y_train as input and returns the coefficients for each feature, along with a plot of the features and their weights.

def lasso_cv_coef(X_train, y_train):
    reg = LassoCV()
    reg.fit(X_train, y_train)
    return reg.coef_

lasso_cv_coef(X_train, y_train)

# 5.) Write 3 functions:
# the first computes the number of optimum features (n) using rfe
def rfe_features(X_train, y_train):
    model = LinearRegression()
    rfe = RFE(model, 2)
    X_rfe = rfe.fit_transform(X_train,y_train) 
    model.fit(X_rfe,y_train)
    return rfe.support_, rfe.ranking_

rfe_features(X_train, y_train)
# the second takes n as input and returns the top n features

# the third takes the list of the top n features as input and returns a new X_train and X_test dataframe with those top features , recursive_feature_elimination() that computes the optimum number of features (n) and returns the top n features.



