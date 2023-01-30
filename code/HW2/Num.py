import math

class Num:
    def __init__(self, at = 0, txt = ""):
        self.at = at
        self.txt = txt
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.lo = math.inf
        self.hi = -math.inf
        self.w = -1 if txt.endswith("-") else 1


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

    
    # MEthod to return a number after rounding it 
    def rnd(self, x, n):
        return x if x == "?" else round(x, n)
    

# nums = Num()
# for num in [1,2,3,4,5,6,7,8,9]:
#     nums.add(num)

# print(f'Mean: {nums.mid()}')
# print(f'STD: {nums.div()}')
# print(f'rnd: {nums.rnd(2.9034567, 4)}')