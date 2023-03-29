import sys
sys.path.insert(1, "../")
from Utils import samples


def testSample():
    for i in range(1,10+1): 
        print("",''.join(samples(["a","b","c","d","e"]).values()))
