import csv
import numpy as np
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import mysql.connector
class Barchart:
    def graph(self):

        algtime= []
        svtime = []
        algacuracy = []

        database = mysql.connector.connect(host="localhost", user="root", passwd="root", db='predict')
        cursor = database.cursor()
        cursor.execute("select timee,acuracy from knn")
        records = cursor.fetchall()
        for row in records:
            algtime.append(float(row[0]));
            algacuracy.append(float(row[1]))
            #print(ktime)
        cursor.execute("select timee,acuracy from svm")
        records1 = cursor.fetchall()
        for row1 in records1:
            algtime.append(float(row1[0]));
            algacuracy.append(float(row1[1]))

        print(algtime)
        plt.rcdefaults()
        objects = ('KNN','SVM')
        #algtime=[100.0,81]
        y_pos = np.arange(len(objects))
        plt.bar(y_pos,algtime, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Seconds')
        plt.title('Predict Time Analysis')
        plt.show()



        objects1 = ('KNN','SVM')
        #algtime=[100.0,81]
        y_pos1= np.arange(len(objects1))
        plt1.bar(y_pos1,algacuracy, align='center', alpha=0.5)
        plt1.xticks(y_pos1, objects1)
        plt1.ylabel('Accuracy')
        plt1.title('Predict Accuracy Analysis')
        plt.show()



if __name__=="__main__":
    bar=Barchart()
    bar.graph()