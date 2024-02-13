import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, accuracy_score


glass_data = pd.read_csv('glass.csv')

x_train = glass_data.drop("Type", axis=1)
y_train = glass_data['Type']


x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=0.2, random_state=0)

gnb = GaussianNB()
gnb.fit(x_train, y_train)


y_pred = gnb.predict(x_test)

qual_report = classification_report(y_test, y_pred)
print(qual_report)
print("Naive Bayes: ",  (accuracy_score(y_test, y_pred))*100)