import csv
import random
import math
from csv import reader
import operator
import  sys
import time
class Predict_Knn:
    def load_data_set(self,filename):
        data=[]
        try:
            '''with open(filename, newline='') as dataset:
            return list(reader(dataset, delimiter=','))'''
            with open(filename) as f:
                reader = csv.reader(f)
                next(reader)  # skip header
                for row in reader:
                    data.append(row)
            return list(data)

        except FileNotFoundError as e:
            raise e
    def euclideanDistance(self,instance1, instance2, length):
        distance = 0
        for x in range(length):
            print("testinstance1["+str(x)+"]",instance1[x])
            print("traininstance1[" + str(x) + "]", instance2[x])
            distance += pow(float(instance1[x]) -float(instance2[x]), 2)
            print("dist=",distance)
        return math.sqrt(distance)

    def getNeighbors(self,trainingSet, testInstance, k):
        try:
            distances = []
            length = len(testInstance)
            print("len=", length)
            print("lentr=",len(trainingSet))
            for x in range(len(trainingSet)):
                dist =self.euclideanDistance(testInstance,trainingSet[x], length)
                distances.append((trainingSet[x], dist))
           # print("dist1=",distances)
            distances.sort(key=operator.itemgetter(1))
            #print("dist=", distances)
            neighbors = []
            for x in range(k):
                print("distances["+str(x)+"]=",distances[x][0])
                neighbors.append(distances[x][0])
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        return neighbors

    def getResponse(self,neighbors):
        classVotes = {}
        for x in range(len(neighbors)):
            response = neighbors[x][-1]
            print("neighbors["+str(x)+"][-1]="+response)

        if response in classVotes:
            classVotes[response] += 1
            print("ifclassVotes[" + str(response) + "]=",classVotes[response])
        else:
            classVotes[response] = 1
            print("elseclassVotes[" + str(response) + "]=",classVotes[response])
        print("cv=", classVotes)
        sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
        print("cvi=", classVotes.items())
        print("s=", sortedVotes)
        return sortedVotes[0][0]

    def getAccuracy(self,testSet, predictions):
        correct = 0
        for x in range(len(testSet)):
            if testSet[x][-1] == predictions[x]:
                correct += 1
        return (correct / float(len(testSet))) * 100.0


    def predict(self,traindata,testdata):
        try:

            trainingSet =self.load_data_set(traindata)
            testSet = self.load_data_set(testdata)
            print("ts=", trainingSet)
            print("tst=", testSet)
            print("tstlen=", len(testSet))
            predictions = []
            k = 3
            for x in range(len(testSet)):
                neighbors =self.getNeighbors(trainingSet, testSet[x], k)
                result =self.getResponse(neighbors)
                predictions.append(result)
                print('>>> Predicted=' + repr(result))
                if (result == '0'):
                    predictval = "Heart Disease Risk:  No"
                    print("Heart Disease Risk:  No")
                if (result == '1'):
                    predictval = "Heart Disease Risk:  Low"
                    print("Heart Disease Risk:  Low")
                if (result == '2' or result == "3"):
                    predictval = "Heart Disease Risk:  Average"
                    print("Heart Disease Risk:  Average")
                if (result == '4'):
                    predictval = "Heart Disease Risk:  High"
                    print("Heart Disease Risk:  High")

            return predictval
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def main(self):
        trainingSet ="heart.csv"
        testSet = "test.csv"
        self.predict(trainingSet,testSet)

if __name__ == "__main__":
    obj=Predict_Knn()
    obj.main()


