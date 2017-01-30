import sys
import random
import pandas as pd
import copy

class PubData():
    globalDataList = []
    currentDataList = []
    currentQuestion = ''
    currentCorrectNumber= 0

    #初始化,从excel文件装载数据，完成问题列表数据初始化
    def __init__(self):
        df = pd.read_excel('q.xlsx')
        aDataList = df['question'].tolist()
        #对象赋值必须使用深拷贝，否则就会变成引用
        PubData.globalDataList = copy.deepcopy(aDataList)
        PubData.currentDataList = copy.deepcopy(aDataList)
        PubData.currentQuestion = ''



        print('initial successful....')

    #随机获取当前问题
    def getCurrentQuestion(self):
          #此处使用self.与使用PubData. 有重大区别
          if len(self.currentDataList) > 0 :
             self.currentQuestion = random.choice(self.currentDataList)
          else:
             self.currentQuestion = 'none'

          return self.currentQuestion

    def testOutPut(self):
        print(self.currentQuestion)


