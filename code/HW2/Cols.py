import re
import Num
import Sym

class Cols:
    def __init__(self,t,col,cols):
        self.names=t
        self.all=[]
        self.x=[]
        self.y=[]
        self.klass=None
        for n,s in enumerate(t):
            col = Num(n,s) if len(re.findall("^[A-Z]+",s)!=0) else Sym(n,s)
        self.all.append(col)
        if len(re.findall("X$",s)==0):
            if len(re.findall("!$",s))!=0:
                self.klass=col
            if len(re.findall("[!+-]$",s)!=0):
                self.y.append(col)
            else:
                self.x.append(col)


    def add(self, row):
        for t in {self.x,self.y}:
            for col in t:
                col.add(row.cells[col.at])
            

