import sys
sys.path.insert(1, "../code")
import Num
#import The
#from Utils import rnd

class TestNum:

    def testNum(self):
        #constructor parameters??
        num = Num.Num()
        #The.cap = 100 #??????????
        li=[1,1,1,1,2,2,3]
        for i in li:
            num.add(i)

        mean = num.mid()
        std = num.div()
        #print("Mid =", mid)
        #print("div =", div)
        return (mean==11/7 and round(std,3)==0.787)
        #Lua has div range between 30.5 to 32 but the answer on calculation comes between 27.5 to 29
        # if(50 <= mid <= 52) and (27.5 < div < 29):
        #     return 0
        # else:
        #     return 1

if __name__ == '__main__':
        result = TestNum.testNum(1)
        print(result)


# eg("num", "check nums", function()
#   local num=NUM()
#   for _,x in pairs{1,1,1,1,2,2,3} do num:add(x) end
#   return 11/7 == num:mid() and 0.787 == rnd(num:div()) end )