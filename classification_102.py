from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
import pandas as pd

uri = "https://gist.githubusercontent.com/guilhermesilveira/2d2efa37d66b6c84a722ea627a897ced/raw/10968b997d885cbded1c92938c7a9912ba41c615/tracking.csv"
data = pd.read_csv(uri)

map = {
    'home': 'home_page',
    'how_it_works': 'about_page',
    'contact': 'contact_page',
    'bought': 'user_bought'
}

data = data.rename(columns=map)

x = data[['home_page', 'about_page', 'contact_page']]
y = data['user_bought']

train_x = x[:75]
train_y = y[:75]
test_x = x[75:]
test_y = y[75:]

print("Training with %d elements and testing with %d elements" %
      (len(train_x), len(test_x)))


SEED = 20

train_x, test_x, train_y, test_y = train_test_split(
    x, y, random_state=SEED, stratify=y, test_size=0.25)


model = LinearSVC()
model.fit(train_x, train_y)

predict = model.predict(test_x)

accuracy = accuracy_score(test_y, predict) * 100
print("The acuraccuracy was %.2f%%" % accuracy)
