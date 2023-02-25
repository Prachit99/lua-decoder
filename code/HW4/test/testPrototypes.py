import Utils
from Constants import Constants
from Data import Data

def testPrototypes():
    file = Constants().file
    t = Utils.doFile(file)
    rows = Utils.repRows(t, Data, Utils.transpose(t['cols']))
    Utils.show(rows.cluster(),"mid",rows.cols.all,1)