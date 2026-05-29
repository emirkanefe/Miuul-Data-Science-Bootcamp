import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.5f' % x)
from mlxtend.frequent_patterns import apriori, association_rules



df_ = pd.read_excel("hafta_5/datasets/online_retail_II.xlsx",
                   sheet_name="Year 2010-2011")
df = df_.copy()
df.head()

df.shape
df.describe().T
df.isnull().sum()

def retail_data_prep(dataframe):
    dataframe.dropna(inplace=True)
    dataframe = dataframe[~dataframe["Invoice"].str.contains("C", na=False)]
    dataframe = dataframe[dataframe["Quantity"] > 0]
    dataframe = dataframe[dataframe["Price"] > 0]
    replace_with_thresholds(dataframe, "Quantity")
    replace_with_thresholds(dataframe, "Price")
    return dataframe

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

df = retail_data_prep(df)

df_fr = df[df["Country"] == "France"]

df_fr.groupby(["Invoice", "Description"]).agg({"Quantity": "sum"}).head(20)

df_fr.groupby(["Invoice", "Description"]).agg({"Quantity": "sum"}).unstack().iloc[0:5, 0:5]

df_fr.groupby(["Invoice", "Description"]).agg({"Quantity": "sum"}).unstack().fillna(0).iloc[0:5, 0:5]

df_fr.groupby(["Invoice", "Description"]).agg({"Quantity": "sum"}).\
    unstack().fillna(0).\
    map(lambda x: 1 if x > 0 else 0).iloc[0:5, 0:5]
####pandas güncellemesi applymap = map


def create_invoice_product_df(dataframe, id=False):
    if id:
        return dataframe.groupby(['Invoice', "StockCode"])['Quantity'].sum().unstack().fillna(0). \
            map(lambda x: 1 if x > 0 else 0)
    else:
        return dataframe.groupby(['Invoice', 'Description'])['Quantity'].sum().unstack().fillna(0). \
            map(lambda x: 1 if x > 0 else 0)

create_invoice_product_df(df_fr)

fr_inv_pro_df = create_invoice_product_df(df_fr)

fr_inv_pro_df = create_invoice_product_df(df_fr, True)
fr_inv_pro_df.head()
def check_id(dataframe, stock_code):
    product_name = dataframe[dataframe["StockCode"] == stock_code]["Description"].iloc[0]
    #product_name = dataframe[dataframe["StockCode"] == stock_code]["Description"].iloc[0]
    print(product_name)

check_id(df_fr, 10120)

####################################
fr_inv_pro_df = fr_inv_pro_df.astype(bool)

frequent_itemsets = apriori(fr_inv_pro_df,
                            min_support=0.01,
                            use_colnames=True)

frequent_itemsets.sort_values("support", ascending=False)

rules = association_rules(frequent_itemsets,
                          metric="support",
                          min_threshold=0.01)
rules.head()

rules[(rules["support"]>0.05) & (rules["confidence"]>0.1) & (rules["lift"]>5)]. \
sort_values("confidence", ascending=False)

check_id(df_fr, 21086)

#########################################################################

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

def retail_data_prep(dataframe):
    dataframe.dropna(inplace=True)
    dataframe = dataframe[~dataframe["Invoice"].str.contains("C", na=False)]
    dataframe = dataframe[dataframe["Quantity"] > 0]
    dataframe = dataframe[dataframe["Price"] > 0]
    replace_with_thresholds(dataframe, "Quantity")
    replace_with_thresholds(dataframe, "Price")
    return dataframe

def create_invoice_product_df(dataframe, id=False):
    if id:
        return dataframe.groupby(['Invoice', "StockCode"])['Quantity'].sum().unstack().fillna(0). \
            map(lambda x: 1 if x > 0 else 0)
    else:
        return dataframe.groupby(['Invoice', 'Description'])['Quantity'].sum().unstack().fillna(0). \
            map(lambda x: 1 if x > 0 else 0)

def check_id(dataframe, stock_code):
    product_name = dataframe[dataframe["StockCode"] == stock_code][["Description"]].values[0].tolist()
    print(product_name)

def create_rules(dataframe, id=True, country="France"):
    dataframe = dataframe[dataframe['Country'] == country]
    dataframe = create_invoice_product_df(dataframe, id)
    dataframe = dataframe.astype(bool)
    frequent_itemsets = apriori(dataframe, min_support=0.01, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="support", min_threshold=0.01)
    return rules

df = df_.copy()

df = retail_data_prep(df)
rules = create_rules(df)

rules[(rules["support"]>0.05) & (rules["confidence"]>0.1) & (rules["lift"]>5)]. \
sort_values("confidence", ascending=False)

#################################################################

#örnek id: 22492

product_id = 22492
check_id(df, product_id)

sorted_rules = rules.sort_values("lift", ascending=False)
recommendations = []

for i, product in enumerate(sorted_rules["antecedents"]):
    for j in list(product):
        if j == product_id:
            recommendations.append(list(sorted_rules.iloc[i]["consequents"])[0])


recommendations[0:5]