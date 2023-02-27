from Constants import Constants 
from Data import Data
from Utils import show


def testCluster():
    file = Constants().file
    data = Data(file)
    show(data.cluster(),"mid",data.cols.y,1)