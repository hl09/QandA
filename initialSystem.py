# coding=utf-8
import pandas as pd
from pubData import *

#使用pubData完成初始化数据，列出当前问题
def initialData():
    pubData = PubData()
    currentQuestion = pubData.getCurrentQuestion()
    print('当前问题：  ' + currentQuestion)

