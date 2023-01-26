import sys
sys.path.insert(1, "../lua")
import Num
from Utils import rand, rnd, SEED

class testRand:

    def testRand(self):
        num1 = Num.Num()
        num2 = Num.Num()
        seed=SEED
        for i in range(1,1001):
            num1.add(rand(0,1))
            num2.add(rand(0,1))
        m1 = rnd(num1.mid(),10)
        m2 = rnd(num2.mid(),10)
        return (m1==m2 and self.rnd(m1,1)==0.5)
