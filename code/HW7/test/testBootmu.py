import sys
sys.path.insert(1, "../")
from Utils import gaussian, cliffsDelta, bootstrap
import numpy as np


def testBootmu():
    a, b = [], []
    for i in range(1,101):
        a.append(gaussian(10,1))
    print("","mu","sd","cliffs","boot","both")
    print("","--","--","------","----","----")
    for mu in np.linspace(10, 11, num = 11):
        b = []
        for i in range(1,101):
            b.append(gaussian(mu,1))
        cl = cliffsDelta(a,b)
        bs = bootstrap(a,b)
        print("", mu, 1, cl, bs, cl and bs)