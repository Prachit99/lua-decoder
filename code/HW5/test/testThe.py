import sys
sys.path.insert(1, "../code")
from Utils import oo
import Constants

class TestThe:
    def testThe(self):
        the = Constants.Constants().the
        return oo(the)


if __name__ == '__main__':
    result = TestThe.testThe(1)
    print(result)