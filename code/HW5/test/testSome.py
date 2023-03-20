import sys
sys.path.insert(1, "../")
import Constants
import Num
from Utils import oo,has

class TestSome:
    def testSome(self):
        Constants.Constants.max=32
        num1=Num()
        for i in range(1,10001):
             num1.add(i)
        oo(has(num1))

if __name__ == '__main__':
        result = TestSome.testSome(1)
        print(result)