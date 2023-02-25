from Utils import repCols
from Data import Data
from Utils import doFile
from Constants import Constants
from Utils import oo


def testRepCols():
    t = repCols(doFile(Constants().file)['cols'], Data)
    cols = list(map(oo, t.cols.all))
    rows = list(map(oo, t.rows))