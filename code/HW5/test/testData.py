import Constants
import Data
from Cols import mid, div
from Utils import stats, oo

def testData():
    file = Constants.Constants().file
    data = Data.Data(file)
    col=data.cols.x[1]
    print(col.lo,col.hi,mid(col),div(col))
    oo(stats(data))


