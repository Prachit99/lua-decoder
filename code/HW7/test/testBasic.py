import sys
sys.path.insert(1, "../")
from Utils import bootstrap, cliffsDelta

def testBasic():
    print("\t\ttruee", 
          bootstrap({8, 7, 6, 2, 5, 8, 7, 3}, {8, 7, 6, 2, 5, 8, 7, 3}), 
          cliffsDelta( {8, 7, 6, 2, 5, 8, 7, 3}, {8, 7, 6, 2, 5, 8, 7, 3}))
    print("\t\tfalse", 
          bootstrap({8, 7, 6, 2, 5, 8, 7, 3}, {9, 9, 7, 8, 10, 9, 6}), 
          cliffsDelta( {8, 7, 6, 2, 5, 8, 7, 3}, {9, 9, 7, 8, 10, 9, 6})) 
    print("\t\tfalse", 
          bootstrap({0.34, 0.49, 0.51, 0.6,   .34,  .49,  .51, .6}, {0.6,  0.7,  0.8,  0.9,   .6,   .7,   .8,  .9}), 
          cliffsDelta({0.34, 0.49, 0.51, 0.6,   .34,  .49,  .51, .6}, {0.6,  0.7,  0.8,  0.9,   .6,   .7,   .8,  .9}))