import sys
sys.path.insert(1, "../")
import Num


def testNum():
    num = Num.Num()
    li=[1,1,1,1,2,2,3]
    for i in li:
        num.add(i)

    mean = num.mid()
    std = num.div()
    return (mean==11/7 and num.rnd(std,3)==0.787)


# if __name__ == '__main__':
#         result = TestNum.testNum(1)
#         print(result)