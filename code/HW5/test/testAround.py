from Constants import Constants
from Data import Data
from Utils import rnd

def testAround():
    file = Constants().file
    data = Data(file)
    print(0,0,data.rows[1].cells)
    for n,t in enumerate(data.around(data.rows[1])):
        if (n % 50) == 0:
            print(n, rnd(t[1],2) ,t[0].cells)