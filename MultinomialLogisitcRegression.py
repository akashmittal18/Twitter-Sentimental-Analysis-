<<<<<<< HEAD
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score
from sklearn.metrics import roc_auc_score


def MultinomialLRAlgo(x_train_vft, y_train, x_test_vft, y_test, vec):
    print("Multinomial Logistic Regression")
    mlr = LogisticRegression(multi_class='multinomial', solver='newton-cg')
    mlr.fit(x_train_vft, y_train)
    y_predict_class = mlr.predict(x_test_vft)
    print("Confusion Matrix")
    print(confusion_matrix(y_test, y_predict_class))
    print('Accuracy Score :', accuracy_score(y_test, y_predict_class))
    print('ROC(Receiver Operating Characteristic) and AUC(Area Under Curve)', roc_auc_score(y_test, y_predict_class))
    print('Average Precision Score:', average_precision_score(y_test, y_predict_class))
    if mlr.predict(vec) == [1]:
        return "Positive"
    else:
=======
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score
from sklearn.metrics import roc_auc_score


def MultinomialLRAlgo(x_train_vft, y_train, x_test_vft, y_test, vec):
    print("Multinomial Logistic Regression")
    mlr = LogisticRegression(multi_class='multinomial', solver='newton-cg')
    mlr.fit(x_train_vft, y_train)
    y_predict_class = mlr.predict(x_test_vft)
    print("Confusion Matrix")
    print(confusion_matrix(y_test, y_predict_class))
    print('Accuracy Score :', accuracy_score(y_test, y_predict_class))
    print('ROC(Receiver Operating Characteristic) and AUC(Area Under Curve)', roc_auc_score(y_test, y_predict_class))
    print('Average Precision Score:', average_precision_score(y_test, y_predict_class))
    if mlr.predict(vec) == [1]:
        return "Positive"
    else:
>>>>>>> a8eac8957e283fe23b26e99d32eac0ba302a4a04
        return "Negative"