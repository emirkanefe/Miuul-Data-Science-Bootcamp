import datetime
import datetime as dt
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from lifetimes import BetaGeoFitter
from lifetimes import GammaGammaFitter
from lifetimes.plotting import plot_period_transactions

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
pd.set_option('display.float_format', lambda x: '%.5f' % x)
from sklearn.preprocessing import MinMaxScaler

###############################################################
# GÖREV 1: Veriyi Hazırlama
###############################################################
df_ = pd.read_csv("hafta_3/datasets/flo_data_20k_cltv.csv")
df = df_.copy()
df.describe().T
df.head()
df.isnull().sum()
df.shape
df.columns
df.nunique()

def outlier_thresholds(dataframe, variable):
    quartile1 = dataframe[variable].quantile(0.01)
    quartile3 = dataframe[variable].quantile(0.99)
    interquantile_range = quartile3 - quartile1
    up_limit = quartile3 + 1.5 * interquantile_range
    low_limit = quartile1 - 1.5 * interquantile_range
    return round(low_limit), round(up_limit)


def replace_with_thresholds(dataframe, variable):
    low_limit, up_limit = outlier_thresholds(dataframe, variable)
    dataframe.loc[(dataframe[variable] < low_limit), variable] = low_limit
    dataframe.loc[(dataframe[variable] > up_limit), variable] = up_limit

outlier_list = ['order_num_total_ever_online', 'order_num_total_ever_offline', 'customer_value_total_ever_offline', 'customer_value_total_ever_online']
for col in outlier_list:
    replace_with_thresholds(df, col)



df["total_order"] = (df["order_num_total_ever_online"] + df["order_num_total_ever_offline"])
df["total_price"] = (df["customer_value_total_ever_online"] + df["customer_value_total_ever_offline"])


df.dtypes

date_columns = ["first_order_date", "last_order_date",  "last_order_date_online", "last_order_date_offline"]
df[date_columns] = df[date_columns].astype("datetime64[ns]")

###############################################################
# GÖREV 2: CLTV Veri Yapısının Oluşturulması
###############################################################
df["last_order_date"].max()

today_date = df["last_order_date"].max() + pd.Timedelta(days= 2)

cltv_df = df.assign(
    customer_id=lambda x: x["master_id"],

    recency_cltv_weekly=lambda x: (x["last_order_date"] - x["first_order_date"]).dt.days / 7,

    T_weekly=lambda x: (today_date - x["first_order_date"]).dt.days / 7,

    frequency=lambda x: x["total_order"],

    monetary_cltv_avg=lambda x: x["total_price"] / x["total_order"]
)[["customer_id", "recency_cltv_weekly", "T_weekly", "frequency", "monetary_cltv_avg"]]

#cltv_df["frequency"] = cltv_df["frequency"].astype(int)
#numeric_cols = cltv_df.select_dtypes(include=np.number).columns
#zero_counts = (cltv_df[numeric_cols] == 0).sum()
#print(zero_counts[zero_counts > 0])
#cltv_df.dtypes

cltv_df.isnull().sum()
#cltv_df = cltv_df[(cltv_df['frequency'] > 1)]
#cltv_df = cltv_df[(cltv_df['recency_cltv_weekly'] > 0)]

#print(df["total_order"].value_counts().sort_index())




###############################################################
# GÖREV 3: BG/NBD, Gamma-Gamma Modellerinin Kurulması, 6 aylık CLTV'nin hesaplanması
###############################################################

bgf = BetaGeoFitter(penalizer_coef=0.01)

bgf.fit(cltv_df['frequency'],
        cltv_df['recency_cltv_weekly'],
        cltv_df['T_weekly'])

bgf.summary

cltv_df["exp_sales_3_month"] =bgf.predict(4 * 3,
                                        cltv_df['frequency'],
                                        cltv_df['recency_cltv_weekly'],
                                        cltv_df['T_weekly']).sort_values(ascending=False)


cltv_df["exp_sales_6_month"] =bgf.predict(4 * 6,
                                        cltv_df['frequency'],
                                        cltv_df['recency_cltv_weekly'],
                                        cltv_df['T_weekly']).sort_values(ascending=False)

cltv_df.sort_values(by="exp_sales_3_month", ascending=False).head(20)

plot_period_transactions(bgf)
plt.show()



## GAMMA GAMMA

ggf = GammaGammaFitter(penalizer_coef=0.01)

ggf.fit(cltv_df['frequency'], cltv_df['monetary_cltv_avg'])

ggf.summary

cltv_df["exp_average_value"] = ggf.conditional_expected_average_profit(cltv_df['frequency'],
                                                                             cltv_df['monetary_cltv_avg'])

cltv_df["cltv"] = ggf.customer_lifetime_value(bgf,
                                   cltv_df['frequency'],
                                   cltv_df['recency_cltv_weekly'],
                                   cltv_df['T_weekly'],
                                   cltv_df['monetary_cltv_avg'],
                                   time=6,  # 6 aylık
                                   freq="W",
                                   discount_rate=0.01)


cltv_df.sort_values(by="cltv", ascending=False).head(20)

#region graph
plt.figure(figsize=(8, 6))
sns.scatterplot(x=cltv_df['monetary_cltv_avg'], y=cltv_df['exp_average_value'])
plt.plot([0, cltv_df['monetary_cltv_avg'].max()], [0, cltv_df['monetary_cltv_avg'].max()], color='red', linestyle='--') # 45 derecelik çizgi
plt.title('Actual vs Predicted Average Order Value')
plt.xlabel('Actual Average Value')
plt.ylabel('Expected Average Value')
plt.show()

cltv_df[["frequency", "monetary_cltv_avg"]].corr()
#endregion
###############################################################
# GÖREV 4: CLTV'ye Göre Segmentlerin Oluşturulması
###############################################################

cltv_final = cltv_df

cltv_final["segment"] = pd.qcut(cltv_final["cltv"], 7, labels=["D", "C", "B", "A"])

cltv_final.groupby("segment").agg({"count", "sum"})