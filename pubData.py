import sys
import random
import pandas as pd

class PubData():
    globalDataList = []
    currentDataList = []
    currentQuestion = ''

    #初始化,从excel文件装载数据，完成问题列表数据初始化
    def __init__(self):
        df = pd.read_excel('q.xlsx')
        aDataList = df['name'].tolist()
        self.globalDataList = aDataList
        self.currentDataList = aDataList
        self.currentQuestion = 'initial....'

        print('initial successful....')

    #随机获取当前问题，并移除队列
    def getCurrentQuestion(self):
        self.currentQuestion = random.choice(self.currentDataList)
        self.currentDataList.remove(self.currentQuestion)
        return self.currentQuestion

    def testOutPut(self):
        print(self.currentQuestion)