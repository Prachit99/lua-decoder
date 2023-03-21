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



egs = {}

def eg(key, s, fun):
    const = Constants.Constants()
    help = const.help
    egs[key] = fun
    help += "  -g  {}\t{}\n".format(key, s)


eg("gauss", "check gauss", testGauss)
eg("num", "check nums", testNum)
eg("basic", "check basic", testBasic)
eg("bootmu", "check bootmu", testBasic)
eg("sample", "check sample", testBasic)
eg("pre", "check pre", testBasic)
eg("five", "check five", testBasic)
eg("six", "check six", testBasic)
eg("sk", "check sk", testBasic)
eg("tiles", "check tiles", testBasic)



const = Constants.Constants()
help = const.help
options = dict()
Main.main(options, help, egs)