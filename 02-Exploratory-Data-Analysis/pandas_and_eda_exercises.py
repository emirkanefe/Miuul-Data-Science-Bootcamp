from sklearn.externals.array_api_extra import nunique

import pandas as pd
import seaborn as sns
import numpy as np

#Görev 1:  Seaborn kütüphanesi içerisinden Titanicveri setini tanımlayınız

df = sns.load_dataset("titanic")
df.shape
df.head(10)
df.info()
df.isnull().values.any()
#Görev 2:  Titanic verisetindeki kadınve erkekyolcuların sayısını bulunuz.

df["sex"].value_counts()

# Görev3:  Her bir sutuna ait unique değerlerin sayısını bulunuz.

df.nunique()
for col in df.columns:
    if df[col].dtype in ["object", "category", "bool"]:
      print (f" {col} : {df[col].nunique()}")

# Görev4:  pclass değişkenini nunique değerlerinin sayısını bulunuz.

df["pclass"].nunique()

# Görev5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz

df[["pclass", "parch"]].nunique()

# Görev6:  embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrolediniz

print(df["embarked"].dtype)

df["embarked"] = df["embarked"].astype("category")

#Görev7:  embarked değeri C olanların tüm bilgelerini gösteriniz.

df.loc[df["embarked"] == "C"]

#Görev8:  embarked değeri S olmayanların tüm bilgelerini gösteriniz.

df.loc[df["embarked"] != "S"]

# Görev9: Yaşı 30dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.

df.loc[(df["sex"] == "female") & (df["age"]  < 30)]


# Görev10:  Fare'i500'den büyük ve ya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.

df.loc[(df["age"] > 70 ) | (df["fare"] > 500)]

#Görev 11:  Her bir değişkendeki boş değerlerin toplamını bulunuz.

df.isnull().sum()

#Görev 12:  who değişkenini dataframe’den çıkarınız.

df.drop("who", axis=1)
df.drop("who", axis=1, inplace=True) #kalıcı olarak çıkarma

#Görev13:  deck değikenindeki boşdeğerleri deck değişkenin en çok tekrareden değeri(mode) ile doldurunuz.

df_mode = df["deck"].mode()[0]

df.loc[df["deck"].isnull(), "deck"] = df_mode

df["deck"].isnull().sum()

#Görev14:  age değikenindeki boşdeğerleri age değişkenin medyanı ile doldurunuz.

df_median = df["age"].median()

df.loc[df["age"].isnull(), "age"] = df_median

df["age"].isnull().sum()

#Görev15:  survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.

df["sex_numeric"] = df["sex"].map({"male": 1, "female": 0})
req = ["sum", "count", "mean"]
df.groupby("survived").agg({"pclass": req,
                            "sex_numeric": req })

#req = ["sum", "count", "mean"]
#df.groupby("survived").agg({"pclass": req,
#                            "sex": ["count"] })

# Görev16:  30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek birfonksiyon yazın.
# Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında birdeğişken oluşturunuz.
# (apply ve lambda yapılarını kullanınız)

def classification(dataframe):
    dataframe["age_flag"] = dataframe["age"].apply(lambda x: 1 if x < 30 else 0)
##  dataframe["age_flag"] = dataframe.loc[:, dataframe.columns.str.contains("age")].apply(lambda x: 1 if x < 30 else 0)


classification(df)

# Görev17:  Seaborn kütüphanesi içerisinden Tipsveri setini tanımlayınız.

df = sns.load_dataset("tips")

# Görev18:  Time değişkeninin kategorilerine(Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz

df.groupby("time").agg({"total_bill": ["describe" ,"sum"] })

# Görev19:  Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.

pd.set_option("display.max_columns", None)

df.groupby(["time","day"]).agg({"total_bill": ["describe" ,"sum"] })

# Görev 20:  Lunch zamanına ve kadın müşterilere ait total_bill ve tip  değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.

target = df.loc[(df["time"] == "Lunch") & (df["sex"] == "Female")]

target.groupby("day").agg({"total_bill": ["describe" ,"sum"] ,
                                "tip" : ["describe" ,"sum"] })

#Görev 21: size'i 3'ten küçük, total_bill'i10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)

target = df.loc[(df["size"] < 3) & (df["total_bill"] > 10)]

target.describe()

# Görev22:  total_bill_tip_sum adında yeni bir değişken oluşturunuz.

df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]

#Görev23:  total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni birdataframe'e atayınız.

df_new = df.sort_values(by="total_bill_tip_sum", ascending=False).head(30).reset_index(drop=True)
len(df_new)



