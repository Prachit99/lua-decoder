import sys
sys.path.insert(1, "../")
import Sym
from Utils import rnd


class TestSym:
    def testSym(self):
        strx = "aaaabbc"
        sym = Sym.Sym()
        for i in range(len(strx)):
            sym.add(strx[i])
        mode = sym.mid()
        entropy = sym.div()
        print(mode,rnd(entropy))
        return 1.38 == rnd(entropy)



# if __name__ == '__main__':
#         result = TestSym.testSym(1)
#         print(result)
