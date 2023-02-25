import sys
sys.path.insert(1, "../")
import Main
import Constants
from testNum import testNum
from testSym import testSym
from testThe import testThe
from testRand import testRand
from testCsv import testCsv
from testData import testData
from testStats import testStats
from testAround import testAround
from testClone import testClone
from testCluster import testCluster
from testHalf import testHalf
from testOptimize import testOptimize


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
eg("data", "check data", testData)
eg("stats", "check stats", testStats)
eg("around","check around",testAround)
eg("clone","check clone",testClone)
eg("cluster","check cluster",testCluster)
eg("half","check half",testHalf)
eg("optimize","check optimize",testOptimize)


const = Constants.Constants()
help = const.help
options = dict()
Main.main(options, help, egs)