import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
import env
from env import user, password, host


def get_titanic_data():
    url = f'mysql+pymysql://{user}:{password}@{host}/titanic_db'
    titanic_data = pd.read_sql('select * from passengers', url)
    return titanic_data

def get_iris_data():
    url = f'mysql+pymysql://{user}:{password}@{host}/iris_db'
    iris_data = pd.read_sql('select * from measurements join species using (species_id)', url)
    return iris_data