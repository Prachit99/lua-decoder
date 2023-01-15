import math

class Sym:
    # Constructor for Sym class
    def __init__(self):
        self.n = 0
        self.has = {}
        self.most = 0
        self.mode = None
    

    # Method to add new symbol of class Sym
    def add(self, x: str):
        if x != "?":
            self.n += 1
            self.has[x] = (self.has[x] + 1) if x in self.has else 1
            if self.has[x] > self.most:
                self.most = self.has[x]
                self.mode = x  
    
    
    # Method to retrun the mode of Sym class 
    def mid(self) -> str:
        return self.mode


    # Method to return the entropy of the class Sym
    def dev(self) -> float:
        def std_form(p):
            return p * math.log(p, 2)
        
        e = 0
        for key,val in self.has.items():
            e += std_form(val/self.n)
        return -e
