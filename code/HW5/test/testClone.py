from Constants import Constants
from Data import Data
from Utils import oo

class TestClone:
    def testClone(self):
        file = Constants().file
        data_1 = Data(file)
        data_2 = data_1.clone(data_1.rows)
        oo(data_1.stats(data_1))
        oo(data_2.stats(data_2))