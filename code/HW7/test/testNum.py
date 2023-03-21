import sys
sys.path.insert(1, "../")
from Num import Num
from Utils import rand


def testNum():
     num = Num()
     for i in range(1,11):
          # num.add(rand(0,1))
          num.add(i)
     print("", num.n, num.mu, num.sd)
     return