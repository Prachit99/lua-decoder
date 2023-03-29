import sys
sys.path.insert(1, "../")
import Main
import Constants
from testNum import testNum
from testBasic import testBasic
from testBootmu import testBootmu
from testFive import testFive
from testGauss import testGauss
from testPre import testPre
from testSample import testSample
from testSix import testSix
from testSk import testSk
from testTiles import testTiles
from testOk import testOk



egs = {}

def eg(key, s, fun):
    const = Constants.Constants()
    help = const.help
    egs[key] = fun
    help += "  -g  {}\t{}\n".format(key, s)

eg("ok","check ok",testOk)
eg("gauss", "check gauss", testGauss)
eg("num", "check nums", testNum)
eg("basic", "check basic", testBasic)
eg("bootmu", "check bootmu", testBootmu)
eg("sample", "check sample", testSample)
eg("pre", "check pre", testPre)
eg("five", "check five", testFive)
eg("six", "check six", testSix)
eg("sk", "check sk", testSk)
eg("tiles", "check tiles", testTiles)



const = Constants.Constants()
help = const.help
options = dict()
Main.main(options, help, egs)