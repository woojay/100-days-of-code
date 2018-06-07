from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

iris = datasets.load_iris()

print( iris.keys() )
print( iris.target_names )
print( iris.feature_names )
print( iris.data[:3])
print( iris.target[:3])
print( iris.data.shape )
print( iris.target.shape )

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)


# test vs predictions
print( y_test )
print( predictions )


# accuracy score, both equal formulas
print( model.score(X_test, y_test))
print( metrics.accuracy_score(y_test, predictions))


# classification report
print( metrics.classification_report(y_test, predictions))

# confusion matrix
print( metrics.confusion_matrix(y_test, predictions))