#Kategorik : sütun, countplot bar
#Sayısal: hist, boxplot
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

df["sex"].value_counts().plot(kind="bar")
plt.show()

#MATPLOTLIB

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df["sex"].value_counts().plot(kind="bar")
plt.show()

plt.hist(df["age"])
plt.show()

plt.boxplot(df["fare"])
plt.show()

x = np.array([1, 8])
y= np.array([0, 150])

plt.plot(x, y)
plt.show()

y = np.array([13, 28, 11, 100])

plt.plot(y, marker = "o")
plt.show()

plt.plot(y, linestyle = "--")
plt.show()

x= np.array([23, 12, 42, 63])
y= np.array([12, 53, 64, 87])
plt.plot(x)
plt.plot(y)
plt.show()


#labels
x= np.array([23, 12, 42, 63])
y= np.array([12, 53, 64, 87])

plt.plot(x, y)
plt.title("Ana başlık")
plt.xlabel("Ana")
plt.ylabel("başlık")
plt.grid(True)
plt.show()

#subplots

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.subplot(1, 2, 1)
plt.title("1")
plt.plot(x, y)
plt.show()

# plot 1
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 1)
plt.title("1")
plt.plot(x, y)

# plot 2
x = np.array([8, 8, 9, 9, 10, 15, 11, 15, 12, 15])
y = np.array([24, 20, 26, 27, 280, 29, 30, 30, 30, 30])
plt.subplot(1, 3, 2)
plt.title("2")
plt.plot(x, y)

# plot 3
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 3)
plt.title("3")
plt.plot(x, y)
plt.show()

#SEABORN

df = sns.load_dataset("tips")
df.head()

df["sex"].value_counts()
sns.countplot(x = df["sex"],data = df)
plt.show()

sns.boxplot(x=df["total_bill"])
plt.show()

sns.histplot(x=df["total_bill"])
plt.show()

df["total_bill"].hist()
plt.show()