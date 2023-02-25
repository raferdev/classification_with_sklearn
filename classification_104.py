from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
import numpy as np
from datetime import datetime
import pandas as pd

uri = "https://gist.githubusercontent.com/guilhermesilveira/4d1d4a16ccbf6ea4e0a64a38a24ec884/raw/afd05cb0c796d18f3f5a6537053ded308ba94bf7/car-prices.csv"
data = pd.read_csv(uri)

yes_no_to_1_0 = {
    'no': 0,
    'yes': 1
}
data.sold = data.sold.map(yes_no_to_1_0)


current_year = datetime.today().year
data['model_age'] = current_year - data.model_year
data['km_per_year'] = data.mileage_per_year * 1.60934

x = data[["price", "model_age", "km_per_year"]]
y = data['sold']


x = data[["price", "model_age", "km_per_year"]]
y = data["sold"]

SEED = 5
np.random.seed(SEED)
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.25,
                                                    stratify=y)
print("Trained with %d elements and test with %d elements" %
      (len(train_x), len(test_x)))

modelo = LinearSVC()
modelo.fit(train_x, train_y)
preddict = modelo.predict(test_x)

acuracia = accuracy_score(test_y, preddict) * 100
print("The accuracy was %.2f%%" % acuracia)


dummy = DummyClassifier()
dummy.fit(train_x, train_y)
preddict = dummy.predict(test_x)

acuracia = accuracy_score(test_y, preddict) * 100
print("The Dummy accuracy was %.2f%%" % acuracia)

dummy_mostfrequent = DummyClassifier(strategy="most_frequent")
dummy_mostfrequent.fit(train_x, train_y)
predict = dummy_mostfrequent.predict(test_x)

acuracia = accuracy_score(test_y, predict) * 100
print("The Dummy (most frequent) accuracy was %.2f%%" % acuracia)
