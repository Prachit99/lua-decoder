from Utils import gaussian
from Num import Num


def testGauss():
    t = []
    for i in range(1, 10**4+1):
        t.append(gaussian(10,2))
    num = Num()
    for i in t:
        num.add(i)
    print("", num.n, num.mu, num.sd)