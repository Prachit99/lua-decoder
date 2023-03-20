from Constants import Constants
from Data import Data

def testHalf():
    file = Constants().file
    data = Data(file)
    left,right,A,B,mid,c = data.half()
    print(len(left),len(right),len(data.rows))
    print(A.cells,c)
    print(mid.cells) 
    print(B.cells)
