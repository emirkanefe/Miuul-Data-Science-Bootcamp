# CLTV = (Customer value / churn rate) * profit margin
# Customer value = Average Order Value * Purchase Freq.
# Average order value = Total Price / Total Transaction
# Purchase Freq. = Total Transaction / Total Number of Customers
# Churn rate = 1 - Repeat Rate
#Profit Margin = Total Price * 0.10

##############################################################################

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

#pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.float_format", lambda x: "%.5f" % x)

df_ = pd.read_excel("hafta_3/datasets/online_retail_II.xlsx", sheet_name="Year 2009-2010")
df = df_.copy()
df.head()
df.shape


df.dropna(inplace = True)
df = df[~df["Invoice"].str.contains("C", na = False)]
df = df[df["Quantity"] > 0]
df.describe().T

df["TotalPrice"] = df["Quantity"] * df["Price"]

cltv_c = df.groupby("Customer ID").agg({"Invoice" : lambda x: x.nunique(),
                                     "Quantity" : lambda x : x.sum(),
                                     "TotalPrice" : lambda TotalPrice : TotalPrice.sum()})

cltv_c.columns = ["total_transaction", "total_unit", "total_price"]

cltv_c["average_order_value"] = cltv_c["total_price"] / cltv_c["total_transaction"]

cltv_c["purchase_freq"] = cltv_c["total_transaction"] / cltv_c.shape[0]

repeat_rate = cltv_c[cltv_c["total_transaction"] > 1].shape[0] / cltv_c.shape[0]

churn_rate = 1 - repeat_rate

cltv_c["profit_margin"] = cltv_c["total_price"]  * 0.10

cltv_c["customer_value"] = cltv_c["average_order_value"] * cltv_c["purchase_freq"]

cltv_c["cltv"] = (cltv_c["customer_value"] / churn_rate) * cltv_c["profit_margin"]

cltv_c.sort_values(by = "cltv", ascending = False).head()

cltv_c["segment"] = pd.qcut(cltv_c["cltv"], 4, labels=["D","C","B","A"])

cltv_c.groupby("segment").agg({"count", "mean", "sum"})

cltv_c.to_csv("cltv_c.csv")


