from spyder_kernels.utils.nsview import default_display

import pandas as pd

s = pd.Series([10, 77, 12, 4, 5])
type(s)
s.index
s.dtype
s.size
s.ndim
s.values
type(s.values)
s.head(3)
s.tail(3)
s.head(-1)

##############################################################################

df = pd.read_csv("hafta_2/advertising.csv")
df.head()


#####################################################################################################################

import seaborn as sns

df = sns.load_dataset("titanic")
df.head()
df.tail()
df.shape
df.info()
df.columns
df.index
df.describe().T
df.isnull().values.any()
df.isnull().sum() # hangi değişkende kaç boş değer var?
df["sex"].head()
df["sex"].value_counts()

#############################################################################
#Seçim işlemleri

df.index
df[0:13]
df.drop(0,axis=0).head()
delete_indexes =[1,3,5,7]
df.drop(delete_indexes,axis=0).head(10)

# df.drop(delete_indexes,axis=0, inplace=True)  KALICI OLARAK DEĞİŞTİRME

df["age"].head()
df.age.head()

df.index = df["age"]

df.drop("age",axis=1, inplace=True)
df.head()

df.index

df["age"] = df.index

df.drop("age",axis=1, inplace=True)

df = df.reset_index().head()

#################################################################################

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")


"age" in df

df["age"].head()

type(df["age"])

df[["age"]].head()
type(df[["age"]]) #dataframe

df[["age", "alive"]]

col_names = ["age", "alive", "adult_male"]

df[col_names].head()

df["age2"] = df["age"] ** 2

df["age3"] = df["age"] / df["age2"]

df.drop("age3", axis=1).head()

df.drop(col_names, axis=1).head()

df.loc[: , ~ df.columns.str.contains("age")].head()

#####################################################################################

df = sns.load_dataset("titanic")

df.iloc[0:3]
df.iloc[0, 0]

df.loc[0:3]

df.iloc[0:3, 0:3]
df.loc[0:3, "age"]

col_names = ["age", "embarked", "alive"]
df.loc[0:3, col_names]

####################################################################################

df = sns.load_dataset("titanic")

df[df["age"]> 50].head()
df[df["age"]> 50]["age"].count()

df.loc[df["age"]>50, ["age", "class"]].head()

df.loc[(df["age"]>50) & (df["sex"] == "male") , ["age", "class"]].head()

df_new = df.loc[(df["age"]>50)
       & (df["sex"] == "male")
       & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")) ,
        ["age", "class", "embark_town"]]

df_new["embark_town"].value_counts()

#########################################################################################

df = sns.load_dataset("titanic")

df["age"].mean()

df.groupby("sex")["age"].mean()

df.groupby("sex").agg({"age": ["mean", "sum"]})

df.groupby("sex").agg({"age": ["mean", "sum"],
                       "survived": ["mean"]})

df.groupby(["sex", "embark_town"]).agg({"age": ["mean", "sum"],
                       "survived": ["mean"]})

df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean", "sum"],
                       "survived": ["mean"]})

df.groupby(["sex", "embark_town", "class"]).agg({
                        "age": ["mean", "sum"],
                       "survived": ["mean"],
                        "sex": "count"})

#############################################################################

df = sns.load_dataset("titanic")


df.pivot_table("survived", "sex", "embarked").head()
df.pivot_table("survived", "sex", ["embarked", "class"]).head()


df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90])

df.pivot_table("survived", "sex",["new_age", "class"])

pd.set_option("display.width", 500)

#############################################################################

df = sns.load_dataset("titanic")

df["age2"] = df["age"]*2
df["age3"] = df["age"]*5

df.head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: x / 10).head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()

df.loc[:,[ "age","age2","age3"]] = df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()

##### herhangi bir fonksiyonu da kullanabilirsin
#############################################################################

import numpy as np
import pandas as pd

m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99

pd.concat([df1, df2],  ignore_index = True)

df1 = pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
                    'group': ['accounting', 'engineering', 'engineering', 'hr']})

df2 = pd.DataFrame({'employees': ['mark', 'john', 'dennis', 'maria'],
                    'start_date': [2010, 2009, 2014, 2019]})

pd.merge(df1, df2)
df3 =pd.merge(df1, df2, on='employees')

df4 = pd.DataFrame({'group': ['accounting', 'engineering', 'hr'],
                    'manager': ['Caner', 'Mustafa', 'Berkcan']})

pd.merge(df3, df4, on='group')

data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)
subset = df.iloc[0:2, [0, 1]]