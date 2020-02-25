import csv
import random
import math
from csv import reader
import operator
import sys
import  time

class Accuracy_Knn:
    def load_data_set(self,filename):
        data = []
        try:
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
            distance += pow(float(instance1[x]) - float(instance2[x]), 2)
            #print("dist=", distance)
        return math.sqrt(distance)


    def getNeighbors(self,trainingSet, testInstance, k):
        try:
            distances = []
            length = len(testInstance)-1

            for x in range(len(trainingSet)):
                dist =self.euclideanDistance(testInstance, trainingSet[x], length)
                distances.append((trainingSet[x], dist))

            distances.sort(key=operator.itemgetter(1))

            neighbors = []
            for x in range(k):
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
            if response in classVotes:
                classVotes[response] += 1
            else:
                classVotes[response] = 1

        sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
        return sortedVotes[0][0]


    def getAccuracy(self,testSet, predictions):
        correct = 0
        for x in range(len(testSet)):
            if testSet[x][-1] == predictions[x]:
                correct += 1
        return (correct / float(len(testSet))) * 100.0

    def accuracy(self,training,testing):
        try:
            trainingSet =self.load_data_set(training)
            testSet =self.load_data_set(testing)
            print("ts=", trainingSet)
            print("tst=", testSet)
            print("tstlen=", len(testSet))
            predictions = []
            k = 3

            for x in range(len(testSet)):
                neighbors =self.getNeighbors(trainingSet, testSet[x], k)
                result =self.getResponse(neighbors)

                predictions.append(result)
                print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))

            accuracy =self.getAccuracy(testSet, predictions)
            print('Accuracy: ' + repr(accuracy) + '%')
            return accuracy

        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def main(self):
        ac=Accuracy_Knn()
        ac.accuracy("heart.csv","testingdata.csv")


if __name__ == "__main__":
    ac = Accuracy_Knn()
    ac.main()


