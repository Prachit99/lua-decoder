from Utils import tiles, scottKnot, RX


def testSix():
    for rx in tiles(scottKnot(
        [RX({101,100,99,101,99.5,101,100,99,101,99.5},"rx1"),
        RX({101,100,99,101,100,101,100,99,101,100},"rx2"),
        RX({101,100,99.5,101,99,101,100,99.5,101,99},"rx3"),
        RX({101,100,99,101,100,101,100,99,101,100},"rx4")])):
        print(f"{rx['name']}\t{rx['rank']}\t{rx['show']}")