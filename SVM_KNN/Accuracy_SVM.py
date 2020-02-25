import numpy as np
from sklearn import preprocessing, cross_validation, neighbors, svm
import pandas as pd
import  sys
from csv import reader
import  csv
import time
class Accuracy_SVM:
    def load__TrainingDataSet(self,training):
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

    def load_TestingData(self,testing):

            try:
                tf = pd.read_csv(testing)
                testdata = np.array(tf.drop(['heartpred'], 1))
                print("td=", testdata)
                return testdata

            except Exception as e:
                raise e

    def getAccuracy(self,testSet, predictions):
        correct = 0
        for x in range(len(testSet)):
            print("predict=",testSet[x])
            print("actual=", predictions[x])
            if testSet[x] == predictions[x]:
                correct += 1
        return (correct / float(len(testSet))) * 100.0

    def predict(self,training,testing):
        try:
            clf=self.load__TrainingDataSet(training)
            testdata =self.load_TestingData(testing)
            testdata = testdata.reshape(len(testdata), -1)
            predictions = clf.predict(testdata)
            print("predictions=",predictions)
            return predictions

        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
    def main(self):
        predictions =self.predict("heart.csv",'testingdata.csv')
        df = pd.read_csv('testingdata.csv')
        testSet = np.array(df['heartpred'])
        accuracy =self.getAccuracy(list(testSet), predictions)
        # print(accuracy)
        print('Accuracy: ' + repr(accuracy) + '%')

if __name__=='__main__':
    acsvm=Accuracy_SVM()
    acsvm.main()