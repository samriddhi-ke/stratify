import pandas as pd

data=pd.read_csv(r"C:\Users\gunem\OneDrive\Desktop\IIT work\order_metadata.csv")
num_orders = data.shape[0]
print("num of orders",num_orders)
abc=data.tail(1)
num_customers=abc['user_id'].values
print("num of customers", num_customers[0])
  
  
