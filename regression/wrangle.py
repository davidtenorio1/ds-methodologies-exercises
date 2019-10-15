import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
import env
from env import user, password, host

url = f'mysql+pymysql://{user}:{password}@{host}/telco_churn'
telco = pd.read_sql("""select customer_id, tenure, monthly_charges, total_charges 
                    from customers 
                    join contract_types using (contract_type_id)
                    where contract_type = 'Two year'""", url)

telco = telco[telco.total_charges != ' ']
telco.total_charges = telco.total_charges.astype(float)


def wrangle_telco():
    charges = pd.read_sql("""select customer_id, tenure, monthly_charges, total_charges 
                    from customers 
                    join contract_types using (contract_type_id)
                    where contract_type = 'Two year'""", url)
    charges = charges[charges.total_charges != ' ']
    charges.total_charges = charges.total_charges.astype(float)
    
    return charges



