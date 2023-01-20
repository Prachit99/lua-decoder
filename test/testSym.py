import sys
sys.path.insert(1, "../code")
import Sym
#from Utils import rnd

class TestSym:

    def testSym(self):
        strx = "aaaabbc"
        #sym.new???????? constructor parameters??
        sym = Sym.Sym()
        for i in range(len(strx)):
            sym.add(strx[i])
        mode = sym.mid()
        entropy = sym.div()
        #entropy = (1000*entropy//1)/1000
        #print(" Mode =", mode)
        #print("Entropy =", entropy)
        return (mode == "a" and 1.379 == round(entropy,3))
#CHECK OBJECTS
if __name__ == '__main__':
        result = TestSym.testSym(1)
        print(result)

# eg("sym","check syms", function()
#   local sym=SYM()
#   for _,x in pairs{"a","a","a","a","b","b","c"} do sym:add(x) end
#   return "a"==sym:mid() and 1.379 == rnd(sym:div())end)