import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df_cust = customers[~customers['id'].isin(orders['customerId'])]
    return df_cust[['name']].rename(columns={'name':'Customers'})