import sys
sys.path.insert(1, "../")
import Constants
import Num
from Utils import oo


def testSome():
    Constants.Constants.max=32
    num1=Num()
    for i in range(1,10001):
            num1.add(i)
    oo(num1.has)

# if __name__ == '__main__':
#         result = TestSome.testSome(1)
#         print(result)