import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from lifetimes import BetaGeoFitter
from lifetimes import GammaGammaFitter
from lifetimes.plotting import plot_period_transactions

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
pd.set_option('display.float_format', lambda x: '%.4f' % x)
from sklearn.preprocessing import MinMaxScaler

###############################################################
# GÖREV 1: Veriyi  Hazırlama ve Anlama (Data Understanding)
###############################################################

df_ = pd.read_csv("hafta_3/datasets/flo_data_20k_rfm.csv")
df = df_.copy()

df.head(10)
df.shape
df.nunique()
df.columns
df.describe().T
df.isnull().sum()
df.dtypes
df.dtypes.value_counts()
df.info

df["total_order"] = (df["order_num_total_ever_online"] + df["order_num_total_ever_offline"])
df["total_price"] = (df["customer_value_total_ever_online"] + df["customer_value_total_ever_offline"])

date_columns = ["first_order_date", "last_order_date",  "last_order_date_online", "last_order_date_offline"]
df[date_columns] = df[date_columns].astype("datetime64[ns]")


date_columns = [col for col in df.columns if "date" in  col]
for col in date_columns:
    df[col] = pd.to_datetime(df[col])

df.groupby("master_id").agg({"master_id": "count",
                            "total_order": "sum",
                            "total_price": "sum",})

df.sort_values(by="total_price", ascending=False, inplace=False).head(10)

df.sort_values(by="total_order", ascending=False, inplace=False).head(10)

def data_preparation(dataframe):

    dataframe["total_order"] = dataframe["order_num_total_ever_online"] + dataframe["order_num_total_ever_offline"]
    dataframe["total_price"] = dataframe["customer_value_total_ever_online"] + dataframe["customer_value_total_ever_offline"]
    date_columns = ["first_order_date", "last_order_date", "last_order_date_online", "last_order_date_offline"]
    dataframe[date_columns] = dataframe[date_columns].astype("datetime64[ns]")
    dataframe.groupby("master_id").agg({"total_order": lambda x: sum(x),
                                 "total_price": lambda x: sum(x), })
    dataframe.sort_values(by="total_price", ascending=False, inplace=False).head(10)
    dataframe.sort_values(by="total_order", ascending=False, inplace=False).head(10)

    return dataframe

###############################################################
# GÖREV 2: RFM Metriklerinin Hesaplanması
###############################################################

df["last_order_date"].max()

today_date = dt.datetime(2021, 6, 1)

rfm = df.groupby("master_id").agg({"last_order_date": lambda date: (today_date - date.max()).days,
                                   "total_order": lambda order: order,
                                   "total_price": lambda price: price})

rfm.columns = ["recency", "frequency", "monetary"]

rfm = rfm[rfm["monetary"] > 0]


###############################################################
# GÖREV 3: RF ve RFM Skorlarının Hesaplanması (Calculating RF and RFM Scores)
###############################################################

rfm["recency_score"] = pd.qcut(rfm["recency"], 5, labels=[5, 4, 3, 2, 1])
rfm["monetary_score"] = pd.qcut(rfm["monetary"], 5, labels=[1, 2, 3, 4, 5])
rfm["frequency_score"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])

rfm["rf_score"] = (rfm["recency_score"].astype(str) + rfm["frequency_score"].astype(str))
rfm["rfm_score"] = (rfm["recency_score"].astype(str) + rfm["frequency_score"].astype(str) + rfm["monetary_score"].astype(str))

###############################################################
# GÖREV 4: RF Skorlarının Segment Olarak Tanımlanması
###############################################################

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

###############################################################
# GÖREV 5: Aksiyon zamanı!
###############################################################

rfm[["segment", "recency", "frequency", "monetary"]].groupby("segment").agg(["mean"])

target_id = rfm[(rfm["segment"] == "champions") | (rfm["segment"] == "loyal_customers")].index

action_a = df[(df["master_id"].isin(target_id)) & (df["interested_in_categories_12"].str.contains("KADIN"))]

action_a.shape

action_a["master_id"].to_csv("case_study_1_a.csv", index=False)

target_id = rfm[(rfm["segment"] == "cant_loose") | (rfm["segment"] == "about_to_sleep") | (rfm["segment"] == "new_customers")].index

action_b = df[(df["master_id"].isin(target_id)) & (df["interested_in_categories_12"].str.contains("COCUK | ERKEK"))]

action_b.shape

action_b["master_id"].to_csv("case_study_1_b.csv", index=False)

