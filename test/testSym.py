import sys
sys.path.insert(1, "../code")
import Sym
#from Utils import rnd

class TestSym:

    def testSym(self):
        strx = "aaaabbc"
        sym = Sym.Sym()
        for i in range(len(strx)):
            sym.add(strx[i])
        mode = sym.mid()
        entropy = sym.div()

        return (mode == "a" and 1.379 == round(entropy,3))
#CHECK OBJECTS
if __name__ == '__main__':
        result = TestSym.testSym(1)
        print(result)
