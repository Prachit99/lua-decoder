import sys
sys.path.insert(1, "../")
import Main
from testNum import TestNum
from testSym import TestSym
from testThe import TestThe
from testRand import TestRand


egs = {}

def eg(key, s, fun):
    global help
    egs[key] = fun
    help += "  -g  {}\t{}\n".format(key, s)


eg("the", "show settings", TestThe.testThe)
eg("rand", "generate, reset, regenerate same", TestRand.testRand)
eg("sym", "check syms", TestSym.testSym)
eg("num", "check nums", TestNum.testNum)
# eg("csv","read from csv", check_csv)
Main.main(egs)