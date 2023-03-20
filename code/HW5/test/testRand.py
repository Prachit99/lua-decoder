import sys
sys.path.insert(1, "../")
from Utils import rand, rnd, seed,rint

class TestRand:
    def testRand(self):
        Seed=1
        t=[]
        for i in range(1,1001):
             t.append(rint(100))
        Seed=1
        u=[]
        for i in range(1,1001):
             u.append(rint(100))
        for k,v in enumerate(t):
             assert(v==u[k])

# if __name__ == '__main__':
#         result = TestRand.testRand(1)
#         print(result)