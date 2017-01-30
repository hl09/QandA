from initialSystem import *
from pubData import *
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from MAIN import Ui_Dialog




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

        #设置每轮计时时间
        global restTime
        restTime = 8

        #设置状态标志，用来控制界面
        global runningFlag
        runningFlag = False

        #创建Qtimer，开始倒计时
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        self.timer.timeout.connect(self.showRestTime)

        #设置控件初始状态
        self.pushButtonWrong.setEnabled(False)
        self.pushButtonRight.setEnabled(False)
        self.pushButtonGo.setEnabled(True)
        self.lcdNumber.display('00:00')
        self.labelCorrectNumber.setText('0')

        #设置字体
        pe = QPalette()
        pe.setColor(QPalette.WindowText, Qt.red)
        self.labelCorrectNumber.setAutoFillBackground(True)
        self.labelCorrectNumber.setPalette(pe)



        #绑定答对按钮处理函数
        self.pushButtonRight.clicked.connect(self.doRightClick)
        #绑定答错按钮处理函数
        self.pushButtonWrong.clicked.connect(self.doWrongClick)
        #绑定开始按钮处理函数
        self.pushButtonGo.clicked.connect(self.doStartClick)

    #处理开始一轮游戏的场景
    def doStartClick(self):
        print('new start...')
        self.pushButtonWrong.setEnabled(True)
        self.pushButtonRight.setEnabled(True)
        self.pushButtonGo.setEnabled(False)

        #设置运行状态
        global runningFlag
        runningFlag = True

        #设置倒计时时间
        global restTime
        restTime = 8
        # 将本轮答对题目数置0，准备好本轮的问题列表，随机抽出当前问题，等待新一轮游戏开始
        pData.currentCorrectNumber = 0
        pData.currentDataList = copy.deepcopy(pData.globalDataList)
        self.labelQ.setText(pData.getCurrentQuestion())


    #处理答对场景，将答对题目移除，并随机抽选下一题.将本轮答对数量加1
    def doRightClick(self):
        print('right button onclicked!')
        pData.currentDataList.remove(pData.currentQuestion)
        pData.globalDataList.remove(pData.currentQuestion)
        pData.currentCorrectNumber = pData.currentCorrectNumber + 1
        self.labelQ.setText(pData.getCurrentQuestion())
        if pData.currentQuestion == 'none':
            QtWidgets.QMessageBox.about(mainfrm, "标题","<p>没有足够的问题可供选择，系统退出！</p>")
            QtWidgets.close()
        self.labelCorrectNumber.setText(str(pData.currentCorrectNumber))



    #处理答错/略过场景，将答错题目从本轮游戏中移除，但总列表保留，并随机抽选下一题
    def doWrongClick(self):
        print('wrong button onclicked!')
        if pData.currentQuestion == 'none':
            QtWidgets.QMessageBox.about(mainfrm, "标题","<p>没有足够的问题可供选择，系统退出！</p>")
            QtWidgets.close()
        pData.currentDataList.remove(pData.currentQuestion)
        self.labelQ.setText(pData.getCurrentQuestion())
        print(pData.currentQuestion)



    # 倒计时，更新时间，在结束时处理界面可用性
    def showRestTime(self):
       #使用运行状态标志来控制界面显示
       global runningFlag
       if runningFlag:
          #全局变量用的时候要指明
          global restTime
          restTime = restTime - 1

          if restTime > 0:
            self.lcdNumber.intValue = restTime

            self.lcdNumber.display(str(self.lcdNumber.intValue))
          else:
            #处理时间结束场景：统计答对数目、设置按钮状态、设置显示、设置倒计时
            print('its time up')
            self.pushButtonRight.setEnabled(False)
            self.pushButtonWrong.setEnabled(False)
            self.pushButtonGo.setEnabled(True)
            QtWidgets.QMessageBox.about(mainfrm, "标题","<p>本轮游戏结束！</p><p>答对题数为："+str(pData.currentCorrectNumber)+"</p>")
            self.lcdNumber.display('00:00')
            self.labelQ.setText('猜！猜！猜！')
            self.labelCorrectNumber.setText('0')
            runningFlag = False

       else:
         self.lcdNumber.display('00:00')


    #空函数，用于处理时间结束
    def doNothing(self):
        pass

pData = initialData()



#运行主窗体
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainfrm = QAWindow()
    mainfrm.show()
    print('gogogogo')
    app.exec_()

