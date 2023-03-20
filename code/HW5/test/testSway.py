import sys
sys.path.insert(1, "../")
import Constants
import Data
from Utils import o,diffs

class TestSway:
    def testSway(self):
        data = Data.Data(Constants.Constants.file)
        best,rest = data.sway()
        print("\nall ", o(data.stats()))
        print("    ", o(data.stats('div')))
        print("\nbest",o(best.stats()))
        print("    ", o(best.stats('div')))
        print("\nrest", o(rest.stats()))
        print("    ", o(rest.stats('div')))
        print("\nall != best?",o(diffs(best.cols.y,data.cols.y)))
        print("best != rest?",o(diffs(best.cols.y,rest.cols.y)))

if __name__ == '__main__':
        result = TestSway.testSway(1)
        print(result)