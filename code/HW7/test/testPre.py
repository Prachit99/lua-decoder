from Utils import gaussian, bootstrap


def testPre():
    print("\neg3")
    d=1
    for i in range(1,10+1):
        t1, t2 = [], []
        for j in range(1, 33):
            t1.append(gaussian(10, 1))
            t2.append(gaussian(10*d, 1))
        val = True if d < 1.1 else False
        print("\t", d, val, bootstrap(t1,t2), bootstrap(t1,t1))
        d += 0.05
        d = round(d, 2)