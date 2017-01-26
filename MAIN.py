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
        self.pushButtonRight = QtWidgets.QPushButton(Dialog)
        self.pushButtonRight.setGeometry(QtCore.QRect(164, 370, 171, 23))
        self.pushButtonRight.setObjectName("pushButtonRight")
        self.pushButtonWrong = QtWidgets.QPushButton(Dialog)
        self.pushButtonWrong.setGeometry(QtCore.QRect(340, 370, 161, 23))
        self.pushButtonWrong.setObjectName("pushButtonWrong")
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(171, 32, 101, 31))
        self.lcdNumber.setAutoFillBackground(False)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(299, 13, 161, 61))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.labelQ = QtWidgets.QLabel(Dialog)
        self.labelQ.setGeometry(QtCore.QRect(260, 180, 161, 101))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(28)
        self.labelQ.setFont(font)
        self.labelQ.setObjectName("labelQ")
        self.labell = QtWidgets.QLabel(Dialog)
        self.labell.setGeometry(QtCore.QRect(28, 21, 141, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(24)
        self.labell.setFont(font)
        self.labell.setObjectName("labell")
        self.pushButtonGo = QtWidgets.QPushButton(Dialog)
        self.pushButtonGo.setGeometry(QtCore.QRect(559, 23, 101, 41))
        self.pushButtonGo.setObjectName("pushButtonGo")
        self.labelCorrectNumber = QtWidgets.QLabel(Dialog)
        self.labelCorrectNumber.setGeometry(QtCore.QRect(451, 20, 71, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(24)
        self.labelCorrectNumber.setFont(font)
        self.labelCorrectNumber.setObjectName("labelCorrectNumber")
        self.pushButtonRight.raise_()
        self.pushButtonWrong.raise_()
        self.labelQ.raise_()
        self.labell.raise_()
        self.label.raise_()
        self.lcdNumber.raise_()
        self.pushButtonGo.raise_()
        self.labelCorrectNumber.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonRight.setText(_translate("Dialog", "答对了！"))
        self.pushButtonWrong.setText(_translate("Dialog", "错/下一题"))
        self.label.setText(_translate("Dialog", "答对题数："))
        self.labelQ.setText(_translate("Dialog", "千里之外"))
        self.labell.setText(_translate("Dialog", "剩余时间："))
        self.pushButtonGo.setText(_translate("Dialog", "开始游戏！"))
        self.labelCorrectNumber.setText(_translate("Dialog", "0"))

