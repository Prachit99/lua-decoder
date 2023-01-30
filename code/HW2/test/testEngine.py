import sys
sys.path.insert(1, "../")
import Main
import Constants
from testNum import TestNum
from testSym import TestSym
# from testThe import TestThe
from testRand import TestRand


egs = {}

def eg(key, s, fun):
    const = Constants.Constants()
    help = const.help
    egs[key] = fun
    help += "  -g  {}\t{}\n".format(key, s)


# eg("the", "show settings", TestThe.testThe)
eg("rand", "check random", TestRand.testRand)
eg("sym", "check syms", TestSym.testSym)
eg("num", "check nums", TestNum.testNum)
# eg("csv","read from csv", check_csv)

const = Constants.Constants()
help = const.help
options = dict()
Main.main(options, help, egs)