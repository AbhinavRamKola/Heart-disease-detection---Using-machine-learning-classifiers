import numpy as np
from sklearn import preprocessing, cross_validation, neighbors, svm
import pandas as pd
import  sys

class Predict_SVM:
    def loadDataSet(self,training):
        try:
            df = pd.read_csv(training)
            X = np.array(df.drop(['heartpred'], 1))# Train  DataSet
            print("X=",X)

            y = np.array(df['heartpred']) #Train Class
            print("y=",y)

            clf = svm.SVC()
            clf.fit(X, y)
            return clf

        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
    def predict(self,training,testing):
        try:
            clf=self.loadDataSet(training)
            tf = pd.read_csv(testing)
            testdata = np.array(tf)
            print("td=",testdata)
            testdata = testdata.reshape(len(testdata), -1)

            result = clf.predict(testdata) # Predicting Heart Disease
            print(">>>Predicted=",result[0])
            if (result[0] == 0):
                predictval = "Heart Disease Risk:  No"
                print("Heart Disease Risk:  No")
            if (result[0] ==1):
                predictval = "Heart Disease Risk:  Low"
                print("Heart Disease Risk:  Low")
            if (result[0] ==2 or result[0] ==3):
                predictval = "Heart Disease Risk:  Average"
                print("Heart Disease Risk:  Average")
            if (result[0] ==4):
                predictval = "Heart Disease Risk:  High"
                print("Heart Disease Risk:  High")
            return predictval
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
if __name__=='__main__':
    svmobj=Predict_SVM()
    svmobj.predict('heart.csv','test.csv')