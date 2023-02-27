from Constants import Constants
import Utils
from Data import Data


def testPosition():
    t = Utils.doFile(Constants().file)
    rows = Utils.repRows(t, Data, Utils.transpose(t['cols']))
    rows.cluster()
    Utils.repPlace(rows)