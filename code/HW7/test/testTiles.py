from Utils import gaussian, RX, tiles, mid


def testTiles():
    rxs, a, b, c, d, e, f, g, h, j, k = [], [], [], [], [], [], [], [], [], [], []
    for z in range(1, 1001):
        a.append(gaussian(10, 1))
    for z in range(1, 1001):
        b.append(gaussian(10.1, 1))
    for z in range(1, 1001):
        c.append(gaussian(20, 1))
    for z in range(1, 1001):
        d.append(gaussian(30, 1))
    for z in range(1, 1001):
        e.append(gaussian(30.1, 1))
    for z in range(1, 1001):
        f.append(gaussian(10, 1))
    for z in range(1, 1001):
        g.append(gaussian(10, 1))
    for z in range(1, 1001):
        h.append(gaussian(40, 1))
    for z in range(1, 1001):
        j.append(gaussian(40, 3))
    for z in range(1, 1001):
        k.append(gaussian(10, 1))
    for k,v in enumerate([a, b, c, d, e, f, g, h, j, k]):
        rxs.append(RX(v,"rx"+str(k+1)))

    for i,x in enumerate(rxs):
        for j,y in enumerate(rxs):
            if mid(x) < mid(y):
                rxs[j],rxs[i]=rxs[i],rxs[j]

    for rx in tiles(rxs):
        print(f"''\t{rx['name']}\t{rx['show']}")