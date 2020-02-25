# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\QT\SVM_KNN\Main1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Predict_Knn import Predict_Knn
from Time_Knn import Time_Knn
from Accuracy_Knn import Accuracy_Knn
from Predict_SVM import Predict_SVM
from Time_SVM import Time_SVM
import pandas as pd
import numpy as np
from Barchart import Barchart
from Accuracy_SVM import Accuracy_SVM
import mysql.connector
class Ui_Dialog(object):
    timee = ""
    acracy = ""
    stime = ""
    sacuracy = ""

    def browsefile_train(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File", "E://", "*.csv")
        print(fileName)
        self.textEdit.setText(fileName)

    def browsefile_test(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File", "E://", "*.csv")
        print(fileName)
        self.textEdit_2.setText(fileName)

    def knn_predict(self):
        try:
            trainingSet = self.textEdit.toPlainText()
            testSet = self.textEdit_2.toPlainText()
            knn = Predict_Knn()
            predictval = knn.predict(trainingSet, testSet)
            tt = Time_Knn()
            st = tt.knn_time(trainingSet, testSet)
            self.timee = st
            self.textEdit_3.setText(predictval + "\n\n" + "Predicting Time: " + str(st) + " s")
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def knn_accuracy(self):
        try:
            trainingSet = self.textEdit.toPlainText()
            testSet = self.textEdit_2.toPlainText()
            ac = Accuracy_Knn()
            res = ac.accuracy(trainingSet, testSet)
            self.acracy = round(res, 3)
            self.textEdit_3.setText("\n" + "Accuracy: " + str(round(res, 3)) + " %")
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def browsefile_train1(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File", "E://", "*.csv")
        print(fileName)
        self.textEdit_4.setText(fileName)

    def browsefile_test1(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File", "E://", "*.csv")
        print(fileName)
        self.textEdit_5.setText(fileName)

    def svm_predcit(self):
        try:
            trainingSet = self.textEdit_4.toPlainText()
            testSet = self.textEdit_5.toPlainText()
            svm = Predict_SVM()
            predictval = svm.predict(trainingSet, testSet)
            stt = Time_SVM()
            svt = stt.svm_time(trainingSet, testSet)
            self.stime = svt
            self.textEdit_6.setText(predictval + "\n\n" + "Predicting Time: " + str(svt) + " s")
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def svm_accuracy(self):
        try:
            trainingSet = self.textEdit_4.toPlainText()
            testSet = self.textEdit_5.toPlainText()
            acsvm = Accuracy_SVM()
            predictions = acsvm.predict(trainingSet, testSet)
            df = pd.read_csv(testSet)
            testSet = np.array(df['heartpred'])
            accuracy = acsvm.getAccuracy(list(testSet), predictions)
            self.sacuracy = accuracy
            # print('Accuracy: ' + repr(accuracy) + '%')
            self.textEdit_6.setText("Accuracy: " + str(round(accuracy, 3)) + " %")
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def viewgraph(self,event):
        bar = Barchart()
        bar.graph()
        event.accept()

    def storeknn(self):
        database = mysql.connector.connect(host="localhost", user="root", passwd="root", db='predict')
        cursor = database.cursor()
        query = "insert into knn values(%s,%s)"
        cursor.execute("delete from knn")
        database.commit()
        values = (self.timee, self.acracy)
        cursor.execute(query, values)
        database.commit()
        print(self.timee)
        print(self.acracy)
        self.textEdit.setText("")
        self.textEdit_2.setText("")
        self.textEdit_3.setText("")
        self.showMessageBox("Information", "Saved Successfully")

    def storesvm(self):
        try:
            database = mysql.connector.connect(host="localhost", user="root", passwd="root", db='predict')
            cursor = database.cursor()
            query = "insert into svm values(%s,%s)"
            cursor.execute("delete from svm")
            database.commit()
            values = (self.stime, self.sacuracy)
            cursor.execute(query, values)
            database.commit()
            self.textEdit_4.setText("")
            self.textEdit_5.setText("")
            self.textEdit_6.setText("")
            self.showMessageBox("Information", "Saved Successfully")
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
    def d(self,event):
        try:
            print("sdsadsad")
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        event.accept()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(584, 520)
        self.graph = QtWidgets.QTabWidget(Dialog)
        self.graph.setGeometry(QtCore.QRect(0, 0, 731, 521))
        self.graph.setMaximumSize(QtCore.QSize(731, 521))
        self.graph.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 75 14pt \"Verdana\";\n"
"")
        self.graph.setObjectName("graph")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(-30, -10, 641, 501))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 581, 491))
        self.label_8.setStyleSheet("image: url(E://QT/heart2.jpg)")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.graph.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(110, 100, 191, 31))
        self.label_2.setStyleSheet("font: 75 12pt \"Verdana\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(110, 130, 221, 31))
        self.textEdit.setObjectName("textEdit")
        self.training = QtWidgets.QPushButton(self.tab_2)
        self.training.setGeometry(QtCore.QRect(350, 132, 71, 31))
        self.training.setStyleSheet("font: 8pt \"Verdana\";")
        self.training.setObjectName("training")
        self.training.clicked.connect(self.browsefile_train)
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(110, 180, 161, 31))
        self.label_3.setStyleSheet("font: 12pt \"Verdana\";")
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_2.setGeometry(QtCore.QRect(110, 210, 221, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.testing = QtWidgets.QPushButton(self.tab_2)
        self.testing.setGeometry(QtCore.QRect(350, 210, 71, 31))
        self.testing.setStyleSheet("font: 8pt \"Verdana\";")
        self.testing.setObjectName("testing")
        self.testing.clicked.connect(self.browsefile_test)
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_3.setGeometry(QtCore.QRect(110, 250, 301, 141))
        self.textEdit_3.setObjectName("textEdit_3")
        self.predict = QtWidgets.QPushButton(self.tab_2)
        self.predict.setGeometry(QtCore.QRect(120, 400, 111, 41))
        self.predict.setObjectName("predict")
        self.predict.clicked.connect(self.knn_predict)
        self.accuracy = QtWidgets.QPushButton(self.tab_2)
        self.accuracy.setGeometry(QtCore.QRect(260, 400, 111, 41))
        self.accuracy.setObjectName("accuracy")
        self.accuracy.clicked.connect(self.knn_accuracy)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(420, 300, 75, 31))
        self.pushButton_5.setStyleSheet("font: 12pt \"Verdana\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.storeknn)
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(170, 40, 231, 31))
        self.label_4.setStyleSheet("color: rgb(85, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.graph.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(130, 120, 161, 31))
        self.label_5.setStyleSheet("font: 12pt \"Verdana\";")
        self.label_5.setObjectName("label_5")
        self.textEdit_4 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_4.setGeometry(QtCore.QRect(130, 150, 221, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        self.pushButton.setGeometry(QtCore.QRect(370, 150, 75, 31))
        self.pushButton.setStyleSheet("font: 10pt \"Verdana\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.browsefile_train1)
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(130, 200, 161, 31))
        self.label_6.setStyleSheet("font: 75 12pt \"Verdana\";")
        self.label_6.setObjectName("label_6")
        self.textEdit_5 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_5.setGeometry(QtCore.QRect(130, 230, 221, 31))
        self.textEdit_5.setObjectName("textEdit_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 230, 75, 31))
        self.pushButton_2.setStyleSheet("font: 75 10pt \"Verdana\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.browsefile_test1)
        self.textEdit_6 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_6.setGeometry(QtCore.QRect(130, 280, 271, 131))
        self.textEdit_6.setObjectName("textEdit_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 430, 121, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.svm_predcit)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_4.setGeometry(QtCore.QRect(270, 430, 121, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.svm_accuracy)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_6.setGeometry(QtCore.QRect(410, 340, 75, 31))
        self.pushButton_6.setStyleSheet("font: 75 12pt \"Verdana\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.storesvm)
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(170, 60, 251, 31))
        self.label_7.setStyleSheet("color: rgb(85, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.graph.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_9 = QtWidgets.QLabel(self.tab_4)
        self.label_9.setGeometry(QtCore.QRect(150, 110, 291, 251))
        self.label_9.setStyleSheet("image: url(E://QT/graph.png);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_9.mousePressEvent=self.viewgraph
        self.graph.addTab(self.tab_4, "")

        self.retranslateUi(Dialog)
        self.graph.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Heart Disease Prediction"))
        self.graph.setTabText(self.graph.indexOf(self.tab), _translate("Dialog", "   Home  "))
        self.label_2.setText(_translate("Dialog", "Training DataSet"))
        self.training.setText(_translate("Dialog", "Browse"))
        self.label_3.setText(_translate("Dialog", "Testing DataSet"))
        self.testing.setText(_translate("Dialog", "Browse"))
        self.predict.setText(_translate("Dialog", "Predicting"))
        self.accuracy.setText(_translate("Dialog", "Accuracy"))
        self.pushButton_5.setText(_translate("Dialog", "Save"))
        self.label_4.setText(_translate("Dialog", "K - Nearest Neighbor"))
        self.graph.setTabText(self.graph.indexOf(self.tab_2), _translate("Dialog", "   KNN  "))
        self.label_5.setText(_translate("Dialog", "Training DataSet"))
        self.pushButton.setText(_translate("Dialog", "Browse"))
        self.label_6.setText(_translate("Dialog", "Testing DataSet"))
        self.pushButton_2.setText(_translate("Dialog", "Browse"))
        self.pushButton_3.setText(_translate("Dialog", "Predicting"))
        self.pushButton_4.setText(_translate("Dialog", "Accuracy"))
        self.pushButton_6.setText(_translate("Dialog", "Save"))
        self.label_7.setText(_translate("Dialog", "Support Vector Machine"))
        self.graph.setTabText(self.graph.indexOf(self.tab_3), _translate("Dialog", "   SVM  "))
        self.graph.setTabText(self.graph.indexOf(self.tab_4), _translate("Dialog", "   Graphs  "))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

