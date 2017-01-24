# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pythonTraining\QandA\MAIN.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(684, 464)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(164, 370, 171, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 370, 161, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(190, 30, 141, 31))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(363, 13, 161, 61))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(260, 180, 161, 101))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.labell = QtWidgets.QLabel(Dialog)
        self.labell.setGeometry(QtCore.QRect(20, 20, 141, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(24)
        self.labell.setFont(font)
        self.labell.setObjectName("labell")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(500, 30, 151, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.lcdNumber.raise_()
        self.labell.raise_()
        self.label.raise_()
        self.textEdit.raise_()
        self.label_2.raise_()
        self.labell.raise_()
        self.labell.raise_()
        self.labell.raise_()
        self.label.raise_()
        self.lcdNumber.raise_()
        self.textEdit.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "答对了！"))
        self.pushButton_2.setText(_translate("Dialog", "错/下一题"))
        self.label.setText(_translate("Dialog", "答对题数"))
        self.label_2.setText(_translate("Dialog", "千里之外"))
        self.labell.setText(_translate("Dialog", "剩余时间"))

