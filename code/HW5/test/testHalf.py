from Constants import Constants
from Data import Data
from Utils import o,stats

class TestHalf:
    def testHalf(self):
        file = Constants().file
        data = Data(file)
        left,right,A,B,mid,c = data.half()
        l,r= data.clone(left),data.clone(right)
        print("l",o(stats(l)))
        print("r",o(stats(r)))


    
