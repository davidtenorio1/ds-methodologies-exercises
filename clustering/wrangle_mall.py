import pandas as pd
from sklearn.model_selection import train_test_split
import env
def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_mall_data():
    return pd.read_sql('SELECT * FROM customers',get_connection('mall_customers'))  


def split_my_data(df,perc_test,random_seed):
    X_train,X_test=train_test_split(df,test_size=perc_test,random_state=random_seed)
    return X_train,X_test
