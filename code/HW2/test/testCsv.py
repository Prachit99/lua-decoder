from Utils import csv
import Constants

class TestCsv:

    def testCsv(self):

        self.n = 0

        def f(t):
            self.n += len(t)

        file = Constants.Constants().file
        csv(file,f)
        return self.n == 8*399
