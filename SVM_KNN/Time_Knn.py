import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import time
class Time_Knn:
    def knn_time(self,training,testing):
        df = pd.read_csv(training)
        X = np.array(df.drop(['heartpred'], 1))# Train  DataSet
        Y =np.array(df['heartpred'])

        knn = KNeighborsClassifier()
        knn.fit(X, Y)

        X_test = pd.read_csv(testing)
        s = time.clock()
        prediction = knn.predict(X_test)
        e = time.clock()
        t=round(e - s,5)
        print("KNN time:=",round(e - s,5), "s")  # the time would be round to 5 decimal in
        return t
if __name__=='__main__':
     tt=Time_Knn()
     tt.knn_time('heart.csv','test.csv')