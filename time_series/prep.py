import pandas as pd
from datetime import timedelta, datetime


def prep_store_data(df):
    # parse the date column and set it as the index
    fmt = '%a, %d %b %Y %H:%M:%S %Z'
    df.sale_date = pd.to_datetime(df.sale_date, format=fmt)
    df = df.sort_values(by='sale_date').set_index('sale_date')

    # add some time components as features
    df['month'] = df.index.strftime('%m-%b')
    df['weekday'] = df.index.strftime('%w-%a')

    # derive the total sales
    df['sales_total'] = df.sale_amount * df.item_price
    return df



def get_sales_by_day(df):
    sales_by_day = df.resample('D')[['sales_total']].sum()
    sales_by_day['diff_with_last_day'] = sales_by_day.sales_total.diff()
    return sales_by_day



def prep_opsd(opsd):
    opsd['Date'] = opsd['Date'].astype('datetime64')
    opsd = opsd.sort_values('Date').set_index('Date')
    opsd['month'] = opsd.index.strftime('%m-%b')
    opsd['year'] = opsd.index.strftime('%Y')
    return opsd