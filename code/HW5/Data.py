from Utils import csv
from Utils import kap
import Utils 
from Row import Row
from Cols import Cols
import math
from Constants import Constants
from operator import itemgetter



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

    
    def furthest(self,row1,rows=None,cols=None):
        t=self.around(row1,rows,cols)
        return t[len(t)-1]

    
    def half(self,rows=None,cols=None,above=None):
        def dist(row1,row2):
            return self.dist(row1,row2,cols)
        
        rows=rows if rows!=None else self.rows
        some=Utils.many(rows,Constants().sample)
        A=above if above != None else Utils.any(some)
        # print(self.furthest(A,rows))
        B=self.furthest(A,rows)[0]
        c=dist(A,B)
        left, right = [], []

        def project(row):
            x, y = Utils.cosine(dist(row,A), dist(row,B), c)
            try:
                row.x = row.x
                row.y = row.y
            except:
                row.x = x
                row.y = y
            return {'row' : row, 'x' : x, 'y' : y}
        for n,tmp in enumerate(sorted(list(map(project, rows)), key=itemgetter('x'))):
            if n < len(rows)//2:
                left.append(tmp['row'])
                mid = tmp['row']
            else:
                right.append(tmp['row'])
        return left, right, A, B, mid, c
    

    def cluster(self,rows=None,cols=None,above=None):
        rows=rows if rows!=None else self.rows
        # minn=minn if minn!=None else pow(len(rows),Constants().min)
        cols=cols if cols!=None else self.cols.x
        node={"data":self.clone(rows)}
        if len(rows)>=2:
            left,right,node["A"],node["B"],node["mid"],node["c"]=self.half(rows,cols,above)
            node["left"]=self.cluster(left,cols,node["A"])
            node["right"]=self.cluster(right,cols,node["B"])
        return node
    

    def sway(self,rows=None,minn=None,cols=None,above=None):
        data = self
        def worker(rows, worse, above = None):
            if len(rows) <= len(data.rows)**Constants().min: 
                return rows, Utils.many(worse, Constants().rest * len(rows))
            else:
                l,r,A,B,_,_ = self.half(rows, None, above)
                if self.better(B,A):
                    l,r,A,B = r,l,B,A
                for row in r:
                    worse.append(row)
                return worker(l,worse,A)
        best,rest = worker(data.rows,[])
        return self.clone(best), self.clone(rest)
    
    def tree(self, rows = None , min = None, cols = None, above = None):
        rows = rows if rows != None else self.rows
        min = min if min != None else len(rows)**Constants().min
        cols = cols if cols != None else self.cols.x
        
        node = { 'data' : self.clone(rows) }
        if len(rows) >= 2*min:
            left, right, node['A'], node['B'], node['mid'], _ = self.half(rows,cols,above)
            node['left']  = self.tree(left,  min, cols, node['A'])
            node['right'] = self.tree(right, min, cols, node['B'])
        return node

