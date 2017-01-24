from initialSystem import *
from pubData import *
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from MAIN import Ui_Dialog



#处理答对场景
def doRight(aData,question):
    aData.currentDataList.remove(question)
    aData.globalDataList.remove(question)
    return aData.getCurrentQuestion()
    pass

#处理答错场景
def doWrong(aData,question):
    aData.currentDataList.remove(question)
    return aData.getCurrentQuestion()

#处理略过场景
def doIgnore(aData,question):
    aData.currentDataList.remove(question)
    return aData.getCurrentQuestion()


class QAWindow(QtWidgets.QWidget,Ui_Dialog):
    def __init__(self):
        super(QAWindow,self).__init__()
        self.setupUi(self)

        global restTime
        restTime = 60

        #创建Qtimer
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        self.timer.timeout.connect(self.showRestTime)

    # 倒计时
    def showRestTime(self):
        #全局变量用的时候要指明
        global restTime
        restTime = restTime - 1
        self.lcdNumber.intValue = restTime
        self.lcdNumber.display(str(self.lcdNumber.intValue))

        if restTime == 0:
            print('its time up')



pData = initialData()
doRight(pData,'财务3')


#运行主窗体
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainfrm = QAWindow()
    mainfrm.show()
    print('gogogogo')
    app.exec_()

