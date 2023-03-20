import sys
sys.path.insert(1, "../")
import Num
import Constants
from Utils import rand,rnd


class TestNum:
    def testNum(self):
        num1,num2 = Num.Num(),Num.Num()
        for i in range(1,10001):
             num1.add(rand())
        for i in range(1,10001):
             num2.add(pow(rand(),2))
        m1,m2=rnd(num1.mid()),rnd(num2.mid())
        d1,d2 = rnd(num1.div()), rnd(num2.div())
        print(1, m1, d1)
        print(2, m2, d2) 
        return m1 > m2 and 0.5 == rnd(m1)


if __name__ == '__main__':
        result = TestNum.testNum(1)
        print(result)

