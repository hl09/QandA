from initialSystem import *
from pubData import *

pData = initialData()

#处理答对场景
def doRight(question):
    pData.currentDataList.remove(question)
    pData.globalDataList.remove(question)
    return pData.getCurrentQuestion()

#处理答错场景
def doWrong(question):
    pData.currentDataList.remove(question)
    return pData.getCurrentQuestion()

#处理略过场景
def doIgnore(question):
    pData.currentDataList.remove(question)
    return pData.getCurrentQuestion()




doRight('财务18')

