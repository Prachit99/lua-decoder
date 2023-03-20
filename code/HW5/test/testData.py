import Constants
import Data

def testData():
    file = Constants.Constants().file
    data = Data.Data(file)
    return len(data.rows) == 398 and data.cols.y[0].w == -1 and data.cols.x[1].at == 1 and len(data.cols.x) == 4