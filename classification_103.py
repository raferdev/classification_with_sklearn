from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC
import seaborn as sns
import pandas as pd

uri = "https://gist.githubusercontent.com/guilhermesilveira/1b7d5475863c15f484ac495bd70975cf/raw/16aff7a0aee67e7c100a2a48b676a2d2d142f646/projects.csv"
data = pd.read_csv(uri)

rename = {
    'expected_hours': 'predicted_hours',
    'price': 'payment',
    'unfinished': 'not_concluded'
}
data = data.rename(columns=rename)
swap = {
    0: 1,
    1: 0
}
data['concluded'] = data.not_concluded.map(swap)


sns.scatterplot(x="predicted_hours", y="payment", hue="concluded", data=data)

sns.relplot(x="predicted_hours", y="payment",
            hue="concluded", col="concluded", data=data)


SEED = 20

x = data[['predicted_hours', 'payment']]
y = data['concluded']

train_x, test_x, train_y, test_y = train_test_split(
    x, y, random_state=SEED, test_size=0.25, stratify=y)

print("We will train with %d elements and test with %d elements" %
      (len(train_x), len(test_x)))

model = LinearSVC(random_state=SEED)
model.fit(train_x, train_y)

predict = model.predict(test_x)

accuracy = accuracy_score(test_y, predict) * 100

print("Test Using LinearSCV")
print("The acuraccuracy was %.2f%%" % accuracy)
print("---------------------------------/n")

baseline_predict = np.ones(540)
accuracy = accuracy_score(test_y, baseline_predict) * 100

print("Baseline test to compare results.")
print(" %.2f%%" % accuracy)
print("---------------------------------/n")

sns.scatterplot(x="predicted_hours", y="payment", hue=test_y, data=test_x)

print("Preprocessing data")
x_min = test_x.predicted_hours.min()
x_max = test_x.predicted_hours.max()
y_min = test_x.payment.min()
y_max = test_x.payment.max()

pixels = 100

x_axis = np.arange(x_min, x_max, (x_max - x_min)/pixels)
y_axis = np.arange(y_min, y_max, (y_max - y_min) / pixels)

xx, yy = np.meshgrid(x_axis, y_axis)

coord = np.c_[xx.ravel(), yy.ravel()]

Z = model.predict(coord)
Z = Z.reshape(xx.shape)

plt.scatter(test_x.predicted_hours, test_x.payment, c=test_y, s=1)
plt.contourf(xx, yy, Z, alpha=0.3)


SEED = 5

np.random.seed(SEED)

x = data[['predicted_hours', 'payment']]
y = data['concluded']

raw_train_x, raw_test_x, train_y, test_y = train_test_split(
    x, y, test_size=0.25, stratify=y)

scaler = StandardScaler()

scaler.fit(raw_train_x)

train_x = scaler.transform(raw_train_x)
test_x = scaler.transform(raw_test_x)
print("Rescaled data to best accuracy using SVC model")

print("We will train with %d elements and test with %d elements" %
      (len(train_x), len(test_x)))

model = SVC(gamma='auto')
model.fit(train_x, train_y)

predict = model.predict(test_x)

accuracy = accuracy_score(test_y, predict) * 100
print("The accuracy was %.2f%%" % accuracy)

data_x = test_x[:, 0]
data_y = test_x[:, 1]

x_min = data_x.min()
x_max = data_x.max()
y_min = data_y.min()
y_max = data_y.max()

pixels = 100

x_axis = np.arange(x_min, x_max, (x_max - x_min)/pixels)
y_axis = np.arange(y_min, y_max, (y_max - y_min) / pixels)

xx, yy = np.meshgrid(x_axis, y_axis)

coord = np.c_[xx.ravel(), yy.ravel()]

Z = model.predict(coord)
Z = Z.reshape(xx.shape)

plt.scatter(data_x, data_y, c=test_y, s=1)
plt.contourf(xx, yy, Z, alpha=0.3)
