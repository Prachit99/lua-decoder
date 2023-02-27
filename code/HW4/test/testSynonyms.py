import Utils
from Data import Data
from Constants import Constants


def testSynonyms():
    data = Data(Constants().file)
    Utils.show(Utils.repCols(Utils.doFile(Constants().file)['cols'], Data).cluster(),"mid",data.cols.all,1)