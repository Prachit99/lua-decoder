from Data import Data
from Constants import Constants

def testStats():
    file = Constants().file
    data = Data(file)

    for k, cols in {'y' : data.cols.y, 'x' : data.cols.x}.items():
        print(k, 'mid', data.stats('mid', cols, 2))
        print(' ', 'div', data.stats('div', cols, 2))
    return True
