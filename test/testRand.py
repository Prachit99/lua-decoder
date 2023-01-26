import sys
sys.path.insert(1, "../code")
import Num
from Utils import rand, rnd, seed
import Main



the = Main.cli(Main.settings(Main.send_help()))

class TestRand:
    def test_rand(self):
        num1 = Num.Num()
        num2 = Num.Num()
        seed=seed
        for i in range(1,1001):
            num1.add(rand(0,1))

        seed = seed
        for i in range(1, 1001):
            num2.add(rand(0,1))

        m1 = rnd(num1.mid(),10)
        m2 = rnd(num2.mid(),10)
        return m1==m2 and rnd(m1,1)==0.5


if __name__ == '__main__':
        result = TestRand.test_rand(1)
        print(result)
