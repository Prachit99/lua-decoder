import sys
sys.path.insert(1, "../lua")
import Num
from Utils import rand, rnd, SEED

class testRand:

    def testRand(self):
        #constructor??????
        num1 = Num.Num()
        num2 = Num.Num()
        #the??????????????
        seed=SEED #seed is the fix var? Seed=937162211
        for i in range(1,1001):
            num1.add(rand(0,1))
            num2.add(rand(0,1))
        m1 = rnd(num1.mid(),10) ## self ki num?? which obj to use??
        m2 = rnd(num2.mid(),10)
        return (m1==m2 and self.rnd(m1,1)==0.5)

#CHECK ALL OBJECTS USED TO CALL FUNCTIONS
            

# eg("rand","generate, reset, regenerate same", function()
#   local num1,num2 = NUM(),NUM()
#   Seed=the.seed; for i=1,10^3 do num1:add( rand(0,1) ) end
#   Seed=the.seed; for i=1,10^3 do num2:add( rand(0,1) ) end
#   local m1,m2 = rnd(num1:mid(),10), rnd(num2:mid(),10)
#   return m1==m2 and .5 == rnd(m1,1) end )