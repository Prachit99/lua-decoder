import sys
sys.path.insert(1, "../code")
from Utils import oo
import Constants
import Main


def testThe():
    the = Constants.Constants().the
    return str(the)


# if __name__ == '__main__':
#     result = TestThe.testThe(1)
#     print(result)