from Utils import csv
from Utils import map
from Utils import kap
from Row import Row
from Cols import Cols

class Data:
    def __init__(self,src,fun):
        self.rows = []
        self.cols = None
        fun=lambda x: self.add(x)
        if type(src)==str:
            csv(src,fun)
        else:
            map(src or [], fun)
    

    def add(self,t):
        if(len(self.cols)!=0):
            if len(t.cells)==0:
                t=Row(t)
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols=Cols(t)


    
    def clone(self,init,data):
        data=Data(list(self.cols.names))
        fun=lambda x: data.add(x)
        map(init or [] ,fun)
        return data


    def stats(self,what,cols,nPlaces):
        def fun(k,col):
            return col.rnd((col,what)(), nPlaces), col.txt
        return kap(cols or self.cols.y, fun)


