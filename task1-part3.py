import pandas as pd

data=pd.read_csv(r"c:\Users\gunem\OneDrive\Desktop\stratify documents\order_items__train.csv")

product_count = data['product_id'].value_counts()
print(product_count.sort_values(ascending=False).head(20))
