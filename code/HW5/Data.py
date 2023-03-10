import Utils 
from Row import Row
from Cols import Cols
import math
import The

class Data:
    def __init__(self,src=None):
        self.rows = []
        self.cols = None
        fun=lambda x: self.add(x)
        if type(src)==str:
            self.csv(src,fun)
        else:
            if(src!=None):
                Utils.csv(src,fun)
            else:
                Utils.map([],fun)
    

    def add(self,t):
        if(len(self.cols)!=0):
            t=Row(t)
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols=Cols(t)


    def clone(self,init=None):
        data=Data(list(self.cols.names))
        fun=lambda x: data.add(x)
        if init:
            Utils.map(init,fun)
        else:
            Utils.map([],fun)
        return data

    def stats(self,what,cols,nPlaces,fun):
        def fun(col):
            temp = getattr(col, what)
            return col.rnd(temp, nPlaces), col.txt
        return Utils.kap(cols, fun)
    

    def dist(self,row1,row2,cols=None):
        n=0
        d=0
        if cols:
            li=cols
        else:
            li=self.cols.x
        for col in li:
            n+=1
            d+=pow(col.dist(row1.cells[col.at],row2.cells[col.at]),The.p)
        return pow((d/n),(1/The.p))
    

    def around(self,row1,rows=None,cols=None):
        if rows!=None:
            li=rows
        else:
            li=self.rows
        around_li=[]
        for r in li:
            around_li.append((r, self.dist(row1, r, cols)))
            around_li.sort(key = lambda x:x[1])
        return around_li
    

    def furthest(self,row1,rows,cols=None):
        t=self.around(row1,rows,cols)
        return t[len(t)]


    def half(self,rows=None,cols=None,above=None):
        some=Utils.many(rows,The.Sample)
        A=above if above != None else Utils.any(some)
        B=self.around(A,some)[The.Far*len(rows)//1].row
        c=self.dist(A,B,cols)
        def project(row,A,B,c,cols):
            return {row,Utils.cosine(self.dist(row,A,cols),self.dist(row,B,cols),c)}
        rows=rows if rows!=None else self.rows
        left=[]
        right=[]
        for n,tmp in enumerate(Utils.sort(Utils.map(rows,project),Utils.lt("dist"))):
            if n<=(len(rows)//2):
                Utils.push(left,tmp.row)
                mid=tmp.row
            else:
                Utils.push(right,tmp.row)
        return left,right,A,B,mid,c
    

    def cluster(self,rows=None,minn=None,cols=None,above=None):
        rows=rows if rows!=None else self.rows
        minn=minn if minn!=None else pow(len(rows),The.minn)
        cols=cols if cols!=None else self.cols.x
        node={"data":self.clone(rows)}
        if len(rows)>2*minn:
            left,right,node["A"],node["B"],node["mid"]=self.half(rows,cols,above)
            node["left"]=self.cluster(left,minn,cols,node["A"])
            node["right"]=self.cluster(right,minn,cols,node["B"])
        return node
    


        



