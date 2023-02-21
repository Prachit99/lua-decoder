import sys
sys.path.insert(1, "../")
import Main
import Constants
from testNum import testNum
from testSym import testSym
from testThe import testThe
from testRand import testRand
from testCsv import testCsv


egs = {}

def eg(key, s, fun):
    const = Constants.Constants()
    help = const.help
    egs[key] = fun
    help += "  -g  {}\t{}\n".format(key, s)


eg("rand", "check random", testRand)
eg("sym", "check syms", testSym)
eg("num", "check nums", testNum)
eg("the", "check the", testThe)
eg("csv", "check csv", testCsv)


const = Constants.Constants()
help = const.help
options = dict()
Main.main(options, help, egs)