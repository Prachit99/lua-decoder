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
from testEvery import testEvery
from testPosition import testPosition
from testPrototypes import testPrototypes
from testRepCols import testRepCols
from testRepRows import testRepRows
from testSynonyms import testSynonyms
from testCopy import testCopy


egs = {}

def eg(key, s, fun):
    const = Constants.Constants()
    help = const.help
    egs[key] = fun
    help += "  -g  {}\t{}\n".format(key, s)


# eg("rand", "check random", testRand)
eg("sym", "check syms", testSym)
eg("num", "check nums", testNum)
eg("the", "check the", testThe)
# eg("csv", "check csv", testCsv)
# eg("data", "check data", testData)
# eg("stats", "check stats", testStats)
# eg("around","check around",testAround)
# eg("clone","check clone",testClone)
# eg("cluster","check cluster",testCluster)
# eg("half","check half",testHalf)
# eg("optimize","check optimize",testOptimize)
eg("copy","check copy",testCopy)
eg("repCols","check repCols",testRepCols)
eg("synonyms","check repcols cluster",testSynonyms)
eg("repRows","check repRows",testRepRows)
eg("prototypes","check prototypes",testPrototypes)
eg("position","check position",testPosition)
eg("every", "check every",testEvery)


const = Constants.Constants()
help = const.help
options = dict()
Main.main(options, help, egs)