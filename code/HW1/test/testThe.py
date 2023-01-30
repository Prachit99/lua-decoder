import sys
sys.path.insert(1, "../code")
from Utils import oo
import Main
the = Main.cli(Main.settings(Main.send_help()))


class TestThe:

    def test_the(self):
        return oo(the)


if __name__ == '__main__':
    result = TestThe.test_the(1)
    print(result)