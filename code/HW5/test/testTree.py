import sys
sys.path.insert(1, "../code")
from Utils import oo
import Constants
import Data


def testTree():
    data=Data.Data(Constants.Constants().file)
    data.showTree(data.tree())


# if __name__ == '__main__':
#     result = TestTree.testTree(1)
#     print(result)