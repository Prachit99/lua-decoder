import Utils
import Constants

class TestCsv:
    n = 0


    def no_of_chars(t):
        global n 
        n += len(t)


    def testCsv(self):
        file = Constants.Constants().file
        Utils.csv(file,TestCsv.no_of_chars)
        return n == 3192
