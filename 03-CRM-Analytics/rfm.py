# 1. İş problemi

import datetime as dt
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", 15)
pd.set_option("display.float_format", lambda x: "%.5f" % x)

df_ = pd.read_excel("hafta_3/datasets/online_retail_II.xlsx", sheet_name="Year 2009-2010")

df = df_.copy()

df.head()
df.shape

df.isnull().sum()

df.nunique()

df["Description"].value_counts().head()
df.groupby("Description").agg({"Quantity" : "sum"}).head()

df.groupby("Description").agg({"Quantity" : "sum"}).sort_values("Quantity", ascending = False).head()

df["Invoice"].nunique()

df["TotalPrice"] = df["Quantity"] * df["Price"]

df.groupby("Invoice").agg({"TotalPrice" : "sum"}).head()

#####################################################################################

df.dropna(inplace = True)

df.describe().T

df = df[~df["Invoice"].str.contains("C", na = False)]

######################################################################################

df.head()

df["InvoiceDate"].max()

today_date = dt.datetime(2010, 12, 11)

type(today_date)

rfm = df.groupby("Customer ID").agg({"InvoiceDate" : lambda date: (today_date - date.max()).days,
                                     "Invoice" : lambda num : num.nunique(),
                                     "TotalPrice" : lambda TotalPrice : TotalPrice.sum()})


rfm.columns = ["recency", "frequency", "monetary"]

rfm.describe().T

rfm = rfm[rfm["monetary"] > 0]

######################################################################################

rfm["recency_score"] = pd.qcut(rfm["recency"], 5, labels=[5, 4, 3, 2, 1])
rfm["monetary_score"] = pd.qcut(rfm["monetary"], 5, labels=[1, 2, 3, 4, 5])
rfm["frequency_score"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])

rfm["rf_score"] = (rfm["recency_score"].astype(str) + rfm["frequency_score"].astype(str))

rfm.describe().T

rfm[rfm["rf_score"] == "11"]

########################################################################################3

seg_map = {
    r'[1-2][1-2]': 'hibernating',
    r'[1-2][3-4]': 'at_Risk',
    r'[1-2]5': 'cant_loose',
    r'3[1-2]': 'about_to_sleep',
    r'33': 'need_attention',
    r'[3-4][4-5]': 'loyal_customers',
    r'41': 'promising',
    r'51': 'new_customers',
    r'[4-5][2-3]': 'potential_loyalists',
    r'5[4-5]': 'champions'
}

rfm["segment"] = rfm["rf_score"].replace(seg_map, regex=True)

rfm[["segment", "recency", "frequency", "monetary"]].groupby("segment").agg(["mean", "count"])

########################################################################################################

rfm[rfm["segment"] == "need_attention"].head()
rfm[rfm["segment"] == "need_attention"].index

new_df = pd.DataFrame()

new_df["new_customer_id"] = rfm[rfm["segment"] == "new_customers"].index

new_df["new_customer_id"] = new_df["new_customer_id"].astype(int)


new_df.to_csv("new_customers.csv")

rfm.to_csv("new_customers.csv")

#############################################################################################################

def create_rfm(dataframe, csv=False):

    # VERIYI HAZIRLAMA
    dataframe["TotalPrice"] = dataframe["Quantity"] * dataframe["Price"]
    dataframe.dropna(inplace=True)
    dataframe = dataframe[~dataframe["Invoice"].str.contains("C", na=False)]

    # RFM METRIKLERININ HESAPLANMASI
    today_date = dt.datetime(2011, 12, 11)
    rfm = dataframe.groupby('Customer ID').agg({'InvoiceDate': lambda date: (today_date - date.max()).days,
                                                'Invoice': lambda num: num.nunique(),
                                                "TotalPrice": lambda price: price.sum()})
    rfm.columns = ['recency', 'frequency', "monetary"]
    rfm = rfm[(rfm['monetary'] > 0)]

    # RFM SKORLARININ HESAPLANMASI
    rfm["recency_score"] = pd.qcut(rfm['recency'], 5, labels=[5, 4, 3, 2, 1])
    rfm["frequency_score"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])
    rfm["monetary_score"] = pd.qcut(rfm['monetary'], 5, labels=[1, 2, 3, 4, 5])

    # cltv_df skorları kategorik değere dönüştürülüp df'e eklendi
    rfm["RFM_SCORE"] = (rfm['recency_score'].astype(str) +
                        rfm['frequency_score'].astype(str))


    # SEGMENTLERIN ISIMLENDIRILMESI
    seg_map = {
        r'[1-2][1-2]': 'hibernating',
        r'[1-2][3-4]': 'at_risk',
        r'[1-2]5': 'cant_loose',
        r'3[1-2]': 'about_to_sleep',
        r'33': 'need_attention',
        r'[3-4][4-5]': 'loyal_customers',
        r'41': 'promising',
        r'51': 'new_customers',
        r'[4-5][2-3]': 'potential_loyalists',
        r'5[4-5]': 'champions'
    }

    rfm['segment'] = rfm['RFM_SCORE'].replace(seg_map, regex=True)
    rfm = rfm[["recency", "frequency", "monetary", "segment"]]
    rfm.index = rfm.index.astype(int)

    if csv:
        rfm.to_csv("rfm.csv")

    return rfm

df = df_.copy()

rfm_new = create_rfm(df, csv=True)


