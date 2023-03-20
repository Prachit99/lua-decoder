import sys
sys.path.insert(1, "../")
import Main
import Constants
from testNum import TestNum
from testSym import TestSym
from testThe import TestThe
from testRand import TestRand
from testSome import TestSome
from testCsv import TestCsv
from testData import TestData
from testClone import TestClone
from testCliffs import TestCliffs
from testDist import TestDist
from testHalf import TestHalf
from testTree import TestTree
from testSway import TestSway
from testBins import TestBins


egs = {}

def eg(key, s, fun):
    const = Constants.Constants()
    help = const.help
    egs[key] = fun
    help += "  -g  {}\t{}\n".format(key, s)


eg("rand", "check random", TestRand.testRand)
eg("sym", "check syms", TestSym.testSym)
eg("num", "check nums", TestNum.testNum)
eg("the", "check the", TestThe.testThe)
eg("some", "demo of reservoir sampling", TestSome.testSome)
eg("csv", "reading csv file", TestCsv.testCsv)
eg("data", "showing data sets", TestData.testData)
eg("clone", "replicate structure of a DATA", TestClone.testClone)
eg("cliffs", "stats tests", TestCliffs.testCliffs)
eg("dist", "distance test", TestDist.testDist)
eg("half", "divide data in half", TestHalf.testHalf)
eg("tree", "show tree of clusters", TestTree.testTree)
eg("sway", "optimizing", TestSway.testSway)
eg("bins", "find deltas between rest and best", TestBins.testBins)



# eg("csv","read from csv", check_csv)

const = Constants.Constants()
help = const.help
options = dict()
Main.main(options, help, egs)