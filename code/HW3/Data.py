from Utils import csv
from Utils import map
from Utils import kap
from Utils import sort
from Utils import cosine
from Utils import many
from Utils import any
from Utils import push
from Utils import lt
from Row import Row
from Cols import Cols
import math
import The

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
    

    def better(self,row1,row2,s1,s2,ys,x,y):
        s1=0
        s2=0
        ys=self.cols.y
        for idx,col in enumerate(ys):
            x=col.norm(row1.cells[col.at])
            y=col.norm(row2.cells[col.at])
            s1=s1-(pow(math.e,(col.w*(x-y))/len(ys)))
            s2=s2-(pow(math.e,(col.w*(y-x))/len(ys)))
        return s1/len(ys) < s2/len(ys)
    

    def dist(self,row1,row2,cols,n,d):
        n=0
        d=0
#?????????? not sure about 'or' in for loop
        for col in cols or self.cols.x:
            n+=1
            d+=pow(col.dist(row1.cells[col.at],row2.cells[col.at]),The.p)
        return pow((d/n),(1/The.p))
    
#AROUND FUNCTION IS MESSY, MOSTLY WRONG????/HELP
    def around(self,row1,rows,cols):
        return sort(map(rows or self.rows, self.around_helper(row1,row2,cols)),lt("dist"))
    

    def around_helper(self,row1,row2,cols):
        return {row2:self.dist(row1,row2,cols)}


    def half(self,rows,cols,above):
        some=many(rows,The.Sample)
        A=above or any(some)
        #CANT FIND // OPERATOR LUA. ASSUMING INT DIVISION
        B=self.around(A,some)[The.Far*len(rows)//1].row
        c=self.dist(A,B,cols)
        def project(row):
        #dictionary doesnt have key's name like lua.just key:value pairs???
            return {row,cosine(self.dist(row,A,cols),self.dist(row,B,cols),c)}
        left=[]
        right=[]
        for n,tmp in enumerate(sort(map(rows,project),lt("dist"))):
            if n<=(len(rows)//2):
                push(left,tmp.row)
                mid=tmp.row
            else:
                push(right,tmp.row)
        return left,right,A,B,mid,c
    

#MANY PYTHON KEYWORDS USED. HAVE TO HANDLE
    def cluster(self,rows,min,cols,above):
        #left and right initialized as empty lists? correct?
        left=[]
        right=[]
        rows=rows or self.rows
        min=min or pow(len(rows),The.min)
        cols=cols or self.cols.x
        node=[self.clone(rows)]
        if len(rows)>2*min:
            left,right,node.A,node.B,node.mid=self.half(rows,cols,above)
            node.left=self.cluster(left,min,cols,node.A)
            node.right=self.cluster(right,min,cols,node.B)
        return node
    

    def sway(self,rows,min,cols,above):
        left=[]
        right=[]
        rows=rows or self.rows
        min=min or pow(len(rows),The.min)
        cols=cols or self.cols.x
        node=[self.clone(rows)]
        if len(rows)>2*min:
            left,right,node.A,node.B,node.mid=self.half(rows,cols,above)
            if self.better(node.B,node.A):
                left,right,node.A,node.B=right,left,node.B,node.A
            node.left=self.sway(left,min,cols,node.A)
        return node


        



