import pandas as pd
import numpy as np
import pydataset
import acquire
import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler



def prep_iris(iris):
    int_encoder = LabelEncoder()
    int_encoder.fit(iris.species)
    iris.species = int_encoder.transform(iris.species)
    return iris


def prep_titanic(iris):
    int_encoder = LabelEncoder()
    int_encoder.fit(titanic.embark_town)
    titanic.embark_town = int_encoder.transform(titanic.embark_town)
    return titanic