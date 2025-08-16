import pandas as pd

department_id_name=pd.read_csv(r"C:\Users\gunem\OneDrive\Desktop\stratify documents\department_info.csv")
aisle_id_name=pd.read_csv(r"C:\Users\gunem\OneDrive\Desktop\stratify documents\aisle_info.csv")
product_aisle_department=pd.read_csv(r"C:\Users\gunem\OneDrive\Desktop\stratify documents\order_items__train.csv")
product_addtocart_reorder=pd.read_csv(r"C:\Users\gunem\OneDrive\Desktop\stratify documents\product_catalog.csv")

df_merged = pd.merge(product_addtocart_reorder,product_aisle_department , on='product_id', how='left')
print(df_merged)

total_orders = df_merged['add_to_cart_order']* (df_merged['reordered']+1)
df_merged['total_orders'] = total_orders
print(df_merged)



df_dept_orders = df_merged.groupby('department_id')['total_orders'].sum().reset_index()
df_dept_orders = df_dept_orders.sort_values(by='total_orders', ascending=False)
print(df_dept_orders)


df_aisle_orders = df_merged.groupby('aisle_id')['total_orders'].sum().reset_index()
df_aisle_orders = df_aisle_orders.sort_values(by='total_orders', ascending=False)
print(df_aisle_orders)


n=10 


top_n_depts = df_dept_orders.head(n)
top_n_depts = pd.merge(top_n_depts, department_id_name, on='department_id', how='left')
top_n_depts = top_n_depts['department']

top_n_aisles = df_aisle_orders.head(n)
top_n_aisles = pd.merge(top_n_aisles, aisle_id_name, on='aisle_id', how='left')
top_n_aisles = top_n_aisles['aisle']

print("Top {} Departments by Total Orders:".format(n),top_n_depts)
print("\nTop {} Aisles by Total Orders:".format(n),top_n_aisles)




