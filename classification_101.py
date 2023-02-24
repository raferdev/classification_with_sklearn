from sklearn.svm import LinearSVC

pig1 = [0, 1, 0]
pig2 = [0, 1, 1]
pig3 = [1, 1, 0]

dog1 = [0, 1, 1]
dog2 = [1, 0, 1]
dog3 = [1, 1, 1]

train_x = [pig1, pig2, pig3, dog1, dog2, dog3]

train_y = [1, 1, 1, 0, 0, 0]

model = LinearSVC()
model.fit(train_x, train_y)

feature1 = [1, 1, 1]
feature2 = [1, 1, 0]
feature3 = [0, 1, 1]

test_x = [feature1, feature2, feature3]
test_y = [0, 1, 1]
predict = model.predict(test_x)

print(predict)
