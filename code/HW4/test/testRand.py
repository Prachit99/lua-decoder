import sys
sys.path.insert(1, "../")
import Num
from Utils import rand, rnd, seed

class TestRand:
    def testRand(self):
        num1 = Num.Num()
        num2 = Num.Num()
        local_seed = seed 
        for i in range(1,1001):
            num1.add(rand(0,1))
            num2.add(rand(0,1))
        m1 = rnd(num1.mid(),1)
        m2 = rnd(num2.mid(),1)
        return (m1==m2 and rnd(m1,1)==0.5)

if __name__ == '__main__':
        result = TestRand.testRand(1)
        print(result)