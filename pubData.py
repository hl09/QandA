import sys
import random
import pandas as pd
import copy

class PubData():
    globalDataList = []
    currentDataList = []
    currentQuestion = ''

    #初始化,从excel文件装载数据，完成问题列表数据初始化
    def __init__(self):
        df = pd.read_excel('q.xlsx')
        aDataList = df['name'].tolist()
        #对象赋值必须使用深拷贝，否则就会变成引用
        PubData.globalDataList = copy.deepcopy(aDataList)
        PubData.currentDataList = copy.deepcopy(aDataList)
        PubData.currentQuestion = 'initial....'



        print('initial successful....')

    #随机获取当前问题
    def getCurrentQuestion(self):
        PubData.currentQuestion = random.choice(PubData.currentDataList)
        return PubData.currentQuestion

    def testOutPut(self):
        print(self.currentQuestion)


