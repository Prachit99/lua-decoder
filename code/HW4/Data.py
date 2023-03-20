from Utils import csv
from Utils import kap
import Utils 
from Row import Row
from Cols import Cols
import math
from Constants import Constants

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


    def clone(self,init={}):
        data=Data([self.cols.names])
        fun=lambda x: data.add(x)
        x=list(map(fun, init))
        return data

    def better(self,row1,row2):
        s1=0
        s2=0
        ys=self.cols.y
        for col in ys:
            x=col.norm(row1.cells[col.at])
            y=col.norm(row2.cells[col.at])
            s1=s1-(pow(math.e,(col.w*(x-y))/len(ys)))
            s2=s2-(pow(math.e,(col.w*(y-x))/len(ys)))
        return s1/len(ys) < s2/len(ys)

    def dist(self,row1,row2,cols=None):
        n=0
        d=0
        if cols:
            li=cols
        else:
            li=self.cols.x
        for col in li:
            n+=1
            d+=pow(col.dist(row1.cells[col.at],row2.cells[col.at]),Constants().p)
        return pow((d/n),(1/Constants().p))
    

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


    def half(self,rows=None,cols=None,above=None):
        rows=rows if rows!=None else self.rows
        some=Utils.many(rows,Constants().sample)
        A=above if above != None else Utils.any(some)
        B=self.around(A,some)[int(Constants().far*len(rows))][0]
        c=self.dist(A,B,cols)
        def project(row):
            return {'row':row,'dist':Utils.cosine(self.dist(row,A,cols),self.dist(row,B,cols),c)}
        left=[]
        right=[]
        fun = lambda x: x['dist']
        for n,tmp in enumerate(Utils.sort(map(project, rows), fun)):
            if n<=(len(rows)//2):
                left.append(tmp['row'])
                mid=tmp['row']
            else:
                right.append(tmp['row'])
        return left,right,A,B,mid,c
    

    def cluster(self,rows=None,minn=None,cols=None,above=None):
        rows=rows if rows!=None else self.rows
        minn=minn if minn!=None else pow(len(rows),Constants().min)
        cols=cols if cols!=None else self.cols.x
        node={"data":self.clone(rows)}
        if len(rows)>=2*minn:
            left,right,node["A"],node["B"],node["mid"],c=self.half(rows,cols,above)
            node["left"]=self.cluster(left,minn,cols,node["A"])
            node["right"]=self.cluster(right,minn,cols,node["B"])
        return node
    

    def sway(self,rows=None,minn=None,cols=None,above=None):
        rows=rows if rows!=None else self.rows
        minn=minn if minn!=None else pow(len(rows),Constants().min)
        cols=cols if cols!=None else self.cols.x
        node={"data":self.clone(rows)}
        if len(rows)>=2*minn:
            left,right,node["A"],node["B"],node["mid"],node["c"]=self.half(rows,cols,above)
            if self.better(node["B"],node["A"]):
                left,right,node["A"],node["B"]=right,left,node["B"],node["A"]
            node['left']=self.sway(left,minn,cols,node["A"])
        return node