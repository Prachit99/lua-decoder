from Constants import Constants
from Data import Data

def testClone():
    file = Constants().file
    data_1 = Data(file)
    data_2 = data_1.clone(data_1.rows)

    return len(data_1.rows) == len(data_2.rows) and data_1.cols.y[1].w == data_2.cols.y[1].w and data_1.cols.x[1].at == data_2.cols.x[1].at and len(data_1.cols.x) == len(data_2.cols.x)