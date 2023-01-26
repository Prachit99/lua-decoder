import math

class Num:
    def __init__(self):
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.lo = math.inf
        self.hi = -math.inf


    # Method to add 
    def add(self, n):
        if n != "?":
            self.n += 1
            d = n - self.mu
            self.mu = self.mu + d/self.n
            self.m2 = self.m2 + d*(n - self.mu)
            self.lo = min(n, self.lo)
            self.hi = max(n, self.hi)


    # Method to return the mean of Num class
    def mid(self):
        return self.mu 


    # Method to return the standard deviation
    def div(self):
        return 0 if (self.m2 < 0 or self.n < 2) else (self.m2/(self.n-1))**(0.5)