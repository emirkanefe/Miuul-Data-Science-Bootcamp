import itertools
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, \
    pearsonr, spearmanr, kendalltau, f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

#Sampling

populasyon = np.random.randint(0, 80, 10000)
populasyon.mean()

np.random.seed(115)

orneklem = np.random.choice(a= populasyon, size= 100)
orneklem.mean()

#Descriptive stat.

df = sns.load_dataset("tips")
df.describe().T

#CI

df.head()

sms.DescrStatsW(df["total_bill"]).tconfint_mean()
sms.DescrStatsW(df["tip"]).tconfint_mean()

df = sns.load_dataset("titanic")
sms.DescrStatsW(df["age"].dropna()).tconfint_mean()
sms.DescrStatsW(df["fare"]).tconfint_mean()

#Corr.

df["total_bill"] = df["total_bill"] - df["tip"]

df.plot.scatter("tip", "total_bill")
plt.show()

df["tip"].corr(df["total_bill"])

#AB testi

df.groupby("smoker").agg({"total_bill": "mean"})

# 1. H0: M1 = M2
#    H1: m1 != M2

# 2.
#Normal mi

test_stat, pvalue = shapiro(df.loc[df["smoker"] == "Yes", "total_bill"])
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue))

test_stat, pvalue = shapiro(df.loc[df["smoker"] == "No", "total_bill"])
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue))

#varyans

test_stat, pvalue = levene(df.loc[df["smoker"] == "Yes", "total_bill"],
                           df.loc[df["smoker"] == "No", "total_bill"])
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue))

#3.

test_stat, pvalue = ttest_ind(df.loc[df["smoker"] == "Yes", "total_bill"],
                              df.loc[df["smoker"] == "No", "total_bill"],
                              equal_var=True)
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue))

test_stat, pvalue = mannwhitneyu(df.loc[df["smoker"] == "Yes", "total_bill"],
                                 df.loc[df["smoker"] == "No", "total_bill"])
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue))

#########################################################################################

df = sns.load_dataset("titanic")

df.groupby("sex").agg({"age": "mean"})

test_stat, pvalue = shapiro(df.loc[df["sex"] == "female", "age"].dropna())
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue))

test_stat, pvalue = shapiro(df.loc[df["sex"] == "male", "age"].dropna())
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue))

test_stat, pvalue = levene(df.loc[df["sex"] == "female", "age"].dropna(),
                           df.loc[df["sex"] == "male", "age"].dropna())
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue))

test_stat, pvalue = mannwhitneyu(df.loc[df["sex"] == "female", "age"].dropna(),
                           df.loc[df["sex"] == "male", "age"].dropna())
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue))

#############################################################################

df =pd.read_csv("hafta_4/datasets/diabetes.csv")
df.head()

df.groupby("Outcome").agg({"Age": "mean"})

test_stat, pvalue = shapiro(df.loc[df["Outcome"] == 1, "Age"].dropna())
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue))

test_stat, pvalue = shapiro(df.loc[df["Outcome"] == 0, "Age"].dropna())
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue))

test_stat, pvalue = mannwhitneyu(df.loc[df["Outcome"] == 1, "Age"].dropna(),
                           df.loc[df["Outcome"] == 0, "Age"].dropna())
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue))

##############################################################################

df =pd.read_csv("hafta_4/datasets/course_reviews.csv")
df.head()

df.groupby("Rating").agg({"Progress": "mean"})

test_stat, pvalue = shapiro(df.loc[df["Progress"] > 75, "Rating"])
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue))

test_stat, pvalue = shapiro(df.loc[df["Progress"] < 25, "Rating"])
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue))

test_stat, pvalue = mannwhitneyu(df[(df["Progress"] >75)]["Rating"],
                                 df[(df["Progress"] <25)]["Rating"])
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue))

###############################################################################

basari_sayisi = np.array([300, 250])
gozlem_sayisi = np.array([1000, 1100])

proportions_ztest(basari_sayisi, gozlem_sayisi)

basari_sayisi / gozlem_sayisi

df = sns.load_dataset("titanic")
df.head()

df.loc[df["sex"] == "female", "survived"].mean()
df.loc[df["sex"] == "male", "survived"].mean()

female_succ_count = df.loc[df["sex"] == "female", "survived"].mean()
female_succ_count = df.loc[df["sex"] == "male", "survived"].mean()

test_stat, pvalue = proportions_ztest(count= [female_succ_count, female_succ_count],
                                      nobs= [df.loc[df["sex"] == "female", "survived"].shape[0],
                                             df.loc[df["sex"] == "male", "survived"].shape[0]])
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue))



















