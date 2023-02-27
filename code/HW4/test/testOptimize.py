from Constants import Constants 
from Data import Data
import Utils


def testOptimize():
    file = Constants().file
    data = Data(file)
    Utils.show(data.sway(),'mid',data.cols.y,1)