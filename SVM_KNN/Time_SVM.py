import numpy as np
from sklearn import preprocessing, cross_validation, neighbors, svm
import pandas as pd
import  sys
import time

class Time_SVM:
    def svm_time(self,training,testing):
        df = pd.read_csv(training)
        X = np.array(df.drop(['heartpred'], 1))# Train  DataSet
        y = np.array(df['heartpred']) #Train Class
        clf = svm.SVC()
        clf.fit(X, y)
        tf = pd.read_csv(testing)
        testdata = np.array(tf)
        testdata = testdata.reshape(len(testdata), -1)
        s = time.clock()
        result= clf.predict(testdata)  # Predicting Heart Disease
        e = time.clock()
        t = round(e - s, 5)
        print("SVM time:", round(e - s, 5), "s")  # the time would be round to 5 decimal in
        return t
if __name__=='__main__':
     tt=Time_SVM()
     tt.svm_time('heart.csv','test.csv')