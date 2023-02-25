from Utils import csv
from Utils import kap
from Row import Row
from Cols import Cols

class Data:
    def __init__(self,src):
        self.rows = []
        self.cols = None
        fun=lambda x: self.add(x)
        if type(src)==str:
            csv(src,fun)
        else:
            for row in src:
                self.add(row)

    def add(self,t):
        if self.cols:
            t = Row(t) if type(t) == list else t
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols=Cols(t)


    def stats(self,what,cols,nPlaces):
        def fun(_, col):
            if what == 'div':
                val = col.div()
            else:
                val = col.mid()
            return col.rnd(val, nPlaces), col.txt
        return kap(cols or self.cols.y, fun)