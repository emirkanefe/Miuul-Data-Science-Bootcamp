import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = pd.read_csv("hafta_2/datasets/breast_cancer.csv")
df = df.iloc[:, 1:-1]
df.head()

num_cols = [col for col in df.columns if df[col].dtype in ["int64", "float64"]]

corr = df[num_cols].corr()

sns.set(rc={'figure.figsize':(12,12)})
sns.heatmap(corr, cmap="RdBu")
plt.show()

# Yüksek korelasyonlu Değişkenlerin Silinmesi

cor_matrix = df[num_cols].corr().abs()

upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(bool))

drop_list = [col for col in upper_triangle_matrix if any(upper_triangle_matrix[col] > 0.90)]

cor_matrix[drop_list]

df.drop(drop_list, axis=1)

def high_correlated_cols(dataframe, plot=False, corr_th=0.90):
    num_cols = [col for col in dataframe.columns if dataframe[col].dtype in ["int64", "float64"]]
    corr = dataframe[num_cols].corr()
    cor_matrix = corr.abs()
    upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(bool))
    drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > corr_th)]
    if plot:
        import seaborn as sns
        import matplotlib.pyplot as plt
        sns.set(rc={'figure.figsize': (15, 15)})
        sns.heatmap(corr, cmap="RdBu")
        plt.show()
    return drop_list

high_correlated_cols(df)
drop_list = high_correlated_cols(df, plot=True)
high_correlated_cols(df.drop(drop_list, axis=1), plot=True)




