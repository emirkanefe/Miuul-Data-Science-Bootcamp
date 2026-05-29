import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.float_format', lambda x: '%.2f' % x)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split, cross_val_score

df = pd.read_csv('hafta_8/datasets/advertising.csv')
df.head()

x = df[["TV"]]
y= df[["sales"]]

reg_model = LinearRegression().fit(x, y)
#y_hat = b + w*x
reg_model.intercept_[0]
reg_model.coef_[0][0]

reg_model.intercept_[0] + reg_model.coef_[0][0]*150

reg_model.intercept_[0] + reg_model.coef_[0][0]*500

df.describe().T

g = sns.regplot(x=x, y=y, scatter_kws={'color': 'b', 's': 9},
                ci=False, color= "r")

g.set_title(f"Model Denklemi: Sales = {round(reg_model.intercept_[0], 2)} + TV*{round(reg_model.coef_[0][0], 2)}")
g.set_ylabel("Satış Sayısı")
g.set_xlabel("TV Harcamaları")
plt.xlim(-10, 310)
plt.ylim(bottom=0)
plt.show()

# tahmin başarısı

#MSE
y_pred = reg_model.predict(x)
mean_squared_error(y, y_pred)
y.mean()
y.std()

#RMSE
np.sqrt(mean_squared_error(y, y_pred))

#MAE
mean_absolute_error(y, y_pred)

#R-Kare
reg_model.score(x, y)

#Multiple linear reg

df = pd.read_csv('hafta_8/datasets/advertising.csv')

x = df.drop('sales', axis=1)
y = df[['sales']]

#Model

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

reg = LinearRegression().fit(x_train, y_train)

# sabit (b- bias)

reg_model.intercept_

#coef. (w - weights)
reg_model.coef_

#TAHMİN

yeni_veri = [[30], [10], [40]]
yeni_veri = pd.DataFrame(yeni_veri).T

reg_model.predict(yeni_veri)

#Tahmin başarısı

#Train RMSE
y_pred = reg_model.predict(x_train)
np.sqrt(mean_squared_error(y_train, y_pred))

# Train rkare
reg_model.score(x_train, y_train)

#test RMSE
y_pred = reg_model.predict(x_test)
np.sqrt(mean_squared_error(y_test, y_pred))

#Test rkare
reg_model.score(x_test, y_test)

#10 katlı cv rmse
np.mean(np.sqrt(-cross_val_score(reg_model,
                                 x,
                                 y,
                                 cv=10,
                                 scoring='neg_mean_squared_error')))

######################################################
# Simple Linear Regression with Gradient Descent from Scratch
######################################################

# Cost function MSE
def cost_function(Y, b, w, X):
    m = len(Y)
    sse = 0

    for i in range(0, m):
        y_hat = b + w * X[i]
        y = Y[i]
        sse += (y_hat - y) ** 2

    mse = sse / m
    return mse


# update_weights
def update_weights(Y, b, w, X, learning_rate):
    m = len(Y)
    b_deriv_sum = 0
    w_deriv_sum = 0
    for i in range(0, m):
        y_hat = b + w * X[i]
        y = Y[i]
        b_deriv_sum += (y_hat - y)
        w_deriv_sum += (y_hat - y) * X[i]
    new_b = b - (learning_rate * 1 / m * b_deriv_sum)
    new_w = w - (learning_rate * 1 / m * w_deriv_sum)
    return new_b, new_w


# train fonksiyonu
def train(Y, initial_b, initial_w, X, learning_rate, num_iters):

    print("Starting gradient descent at b = {0}, w = {1}, mse = {2}".format(initial_b, initial_w,
                                                                   cost_function(Y, initial_b, initial_w, X)))

    b = initial_b
    w = initial_w
    cost_history = []

    for i in range(num_iters):
        b, w = update_weights(Y, b, w, X, learning_rate)
        mse = cost_function(Y, b, w, X)
        cost_history.append(mse)


        if i % 100 == 0:
            print("iter={:d}    b={:.2f}    w={:.4f}    mse={:.4}".format(i, b, w, mse))


    print("After {0} iterations b = {1}, w = {2}, mse = {3}".format(num_iters, b, w, cost_function(Y, b, w, X)))
    return cost_history, b, w


df = pd.read_csv("hafta_8/datasets/advertising.csv")

X = df["radio"]
Y = df["sales"]

# hyperparameters
learning_rate = 0.001
initial_b = 0.001
initial_w = 0.001
num_iters = 100000

cost_history, b, w = train(Y, initial_b, initial_w, X, learning_rate, num_iters)

