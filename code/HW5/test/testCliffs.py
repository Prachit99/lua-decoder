import sys
sys.path.insert(1, "../")
from Utils import  rnd,rand,cliffsDelta
#assumed cliffsDelta going to be written in utils
class TestCliffs:
    def testCliffs(self):
        assert(False == cliffsDelta( [8,7,6,2,5,8,7,3],[8,7,6,2,5,8,7,3]),"1")
        assert(True  == cliffsDelta( [8,7,6,2,5,8,7,3], [9,9,7,8,10,9,6]),"2") 
        t1,t2=[],[]
        for i in range(1,1001):
            t1.append(rand())
        for i in range(1,1001):
            t2.append(pow(rand(),0.5))
        assert(False == cliffsDelta(t1,t1),"3") 
        assert(True  == cliffsDelta(t1,t2),"4") 
        diff,j=False,1.0
        while not diff:
            t3=list(map(lambda x: x*j, t1))
            diff=cliffsDelta(t1,t3)
            print(">",rnd(j),diff) 
            j=j*1.025

if __name__ == '__main__':
        result = TestCliffs.testCliffs(1)
        print(result)