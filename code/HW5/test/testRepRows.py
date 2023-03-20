import Utils
from Constants import Constants
from Data import Data
def testRepRows():
    t=Utils.doFile(Constants().file)
    rows = Utils.repRows(t, Data, Utils.transpose(t['cols']))
    cols = list(map(Utils.oo, rows.cols.all))
    rows = list(map(Utils.oo, rows.rows))