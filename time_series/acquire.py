import requests
import pandas as pd
# base url
base_url = 'https://python.zach.lol'
response = requests.get(base_url + '/api/v1/items')
data = response.json()
payload = pd.DataFrame(data['payload'])
# documentation
documentation = requests.get(base_url + '/documentation')
print(documentation.json()['payload'])

# 1.) Using the code from the lesson as a guide, create a dataframe named items that has all of the data for items.
# first page items

"""items = pd.DataFrame(data['payload']['items'])
# add page 2
response = requests.get(base_url + data['payload']['next_page'])
data = response.json()
print('max_page: %s' % data['payload']['max_page'])
print('next_page: %s' % data['payload']['next_page'])
items = pd.concat([items, pd.DataFrame(data['payload']['items'])]).reset_index()
# add third page
response = requests.get(base_url + data['payload']['next_page'])
data = response.json()
print('max_page: %s' % data['payload']['max_page'])
print('next_page: %s' % data['payload']['next_page'])
items = pd.concat([items, pd.DataFrame(data['payload']['items'])]).reset_index()
items.to_csv(r'items.csv')"""

def get_items():
    base_url = 'https://python.zach.lol'
    items_df = pd.DataFrame()
    for i in range (1,4):
        response = requests.get(base_url + '/api/v1/items?page=' + str(i))
        response = response.json()
        items_df = items_df.append(pd.DataFrame(response['payload']['items']))
    items_df.to_csv(r'items.csv')


# 2.) Do the same thing, but for stores.

def get_stores():
    base_url = 'https://python.zach.lol'
    response = requests.get(base_url + '/api/v1/stores')
    data = response.json()
    stores = pd.DataFrame(data['payload']['stores'])
    stores.to_csv(r'stores.csv')



# 3.) Extract the data for sales. There are a lot of pages of data here, so your code will need to be a little more complex. Your code should continue fetching data from the next page until all of the data is extracted.

response = requests.get(base_url + '/api/v1/sales')
data = response.json()

def get_sales():
    base_url = 'https://python.zach.lol'
    sales_df = pd.DataFrame()
    for p in range (1,184):
        response = requests.get(base_url + '/api/v1/sales?page=' + str(p))
        response = response.json()
        sales_df = sales_df.append(pd.DataFrame(response['payload']['sales']))
        print(183-p)
    sales_df.to_csv(r'sales.csv')


# 4.) Save the data in your files to local csv files so that it will be faster to access in the future.

# done on previous lines

# 5.) Combine the data from your three separate dataframes into one large dataframe.

def combine():
    get_items()
    get_stores()
    get_sales()
    items = pd.read_csv('items.csv')
    stores = pd.read_csv('stores.csv')
    sales = pd.read_csv('sales.csv')
    data = pd.merge(sales,stores,how='left')
    data = pd.merge(data,items,how='left')
    return data

combine()


# 6.) Acquire the Open Power Systems Data for Germany, which has been rapidly expanding its renewable energy production in recent years. The data set includes country-wide totals of electricity consumption, wind power production, and solar power production for 2006-2017. You can get the data here: https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv

# 7.) Make sure all the work that you have done above is reproducible. That is, you should put the code above into separate functions in the acquire.py file and be able to re-run the functions and get the same data.
# done on previous lines













