import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# region GÖREV 1 Aşağıdaki Soruları Yanıtlayınız


#Soru 1: persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.

df = pd.read_csv("datasets/persona.csv")
df.head()
df.isnull()

#Soru 2: Kaç unique SOURCE vardır? Frekansları nedir?

df["SOURCE"].nunique()
df["SOURCE"].value_counts() / len(df) * 100



#Soru 3:Kaç unique PRICE vardır?

df["PRICE"].nunique()

#Soru 4:Hangi PRICE'dan kaçar tane satış gerçekleşmiş?

df["PRICE"].value_counts()

#Soru 5:Hangi ülkeden kaçar tane satış olmuş?

df["COUNTRY"].value_counts()

#Soru 6:Ülkelere göre satışlardan toplam ne kadar kazanılmış?

df.groupby("COUNTRY").agg({ "PRICE": "sum"})

#Soru 7:SOURCE türlerine göre satış sayıları nedir?

df["SOURCE"].value_counts()

#Soru 8:Ülkelere göre PRICE ortalamaları nedir?

df.groupby("COUNTRY").agg({ "PRICE": "mean"})

#Soru 9:SOURCE'lara göre PRICE ortalamaları nedir?

df.groupby("SOURCE").agg({ "PRICE": "mean"})

#Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?

df.groupby(["SOURCE", "COUNTRY"]).agg({ "PRICE": "mean"})
# endregion

#region GÖREV 2 COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?



df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({ "PRICE": "mean"})

#endregion

#region GÖREV 3 ÇıktıyıPRICE’agöre sıralayınız.



agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({ "PRICE": "mean"}).sort_values(by="PRICE", ascending=False)
agg_df.head()
agg_df.shape
#endregion

#region GÖREV 4 Indeksteyer alan isimleri değişken ismine çeviriniz

agg_df = agg_df.reset_index()
agg_df.head()

#endregion

#region GÖREV 5 Age değişkenini kategorik değişkene çeviriniz ve agg_df’eekleyiniz.



agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], bins= [0, 18, 23, 30, 40, agg_df["AGE"].max()], labels=['0_18', '19_23', '24_30', '31_40', f"41_{agg_df['AGE'].max()}"])
agg_df.head()


#endregion

#region Görev 6:  Yeni seviye tabanlı müşterileri (persona) tanımlayınız

def create_persona(agg_df):
    persona = f"{agg_df['COUNTRY']}_{agg_df['SOURCE']}_{agg_df['SEX']}_{agg_df['AGE_CAT']}".upper()
    return persona

agg_df["customers_level_based"] = agg_df.apply(create_persona, axis=1)

agg_df2 = agg_df.groupby("customers_level_based").agg({"PRICE": ["mean"]})
agg_df2 = agg_df.reset_index()
agg_df2.head()
agg_df2.shape
#endregion

#region Görev 7:  Yeni müşterileri (personaları) segmentlere ayırınız.

agg_df2["SEGMENT"] = pd.qcut(agg_df2["PRICE"], 4, labels=["En az kazandıran", "Az kazandıran", "Çok kazandıran", "En çok kazandıran"])

segment_summary = agg_df2.groupby(["SEGMENT", "customers_level_based"]).agg({"PRICE": ["mean", "max", "sum"]})
segment_summary = agg_df2.groupby(["SEGMENT", "customers_level_based"]).agg({"PRICE": ["mean"]})


segment_summary.head()
segment_summary.reset_index()
segment_summary.nunique()



#endregion

#region Görev 8:  Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini  tahmin ediniz.

#Hedeflenen çıktı

final_df = agg_df2[["customers_level_based", "PRICE", "SEGMENT"]]
final_df.nunique()
def predict(dataframe, str):

    prediction = dataframe[dataframe["customers_level_based"] == str]
    avg_price = prediction["PRICE"].mean()
    segment = prediction["SEGMENT"].mode()[0]
    return f"ORTALMA GETİRİSİ:{avg_price}",f"SEGMENTİ: {segment}"


predict(final_df, "FRA_IOS_MALE_31_40")

# new_user = "TUR_ANDROID_FEMALE_31_40"
# new_user = "FRA_IOS_FEMALE_31_40"
# final_df[final_df["customers_level_based"] == new_user]

#endregion



