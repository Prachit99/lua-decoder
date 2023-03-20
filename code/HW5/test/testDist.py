import Constants
import Data
import Num
from Num import mid, div
from Utils import  oo,rnd

class testDist:
    def testDist(self):
        file = Constants.Constants().file
        data = Data.Data(file)
        num=Num()
        for row in data.rows:
            Num.add(num,Data.dist(row,data.rows[1]))
        oo(lo=num.lo,hi=num.hi,mid=rnd(mid(num)),div=rnd(div(num)))
        