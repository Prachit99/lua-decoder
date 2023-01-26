import math

# Utility functions for numerics
seed = 937162211

def rint(lo,hi):
    return math.floor(0.5 + rand(lo,hi))

def rand(lo=0,hi=1):
    global seed
    seed = (16807 * seed) % 2147483647
    # print(seed)
    return lo + (hi - lo) * seed / 2147483647
def rnd(n,nPlaces=3):
    mult = 10**(nPlaces)
    return math.floor(n * mult + 0.5) / mult

# Utility functions for Strings
def fmt(**sControl):
    return print(sControl)

def o(t,isKeys):
    if type(t) != list:
        return str(t)
    def fun(k,v):
        if not str(k).find('^_'):
            return fmt(":{} {}",o(k),o(v))



def oo(t):
    print(o(t))
    return t

def coerce(s):
    def fun(s1):
        return True if s1 == "true" else False
        return s1



# Utility functions for Lists
def map(t,fun):
    u = []
    for k,v in enumerate(t):
        v,k = fun(k)
        index = k if k != 0 else 1+len(u)
        u[index] = v
    return u

def kap(t,fun):
    u = []
    for k,v in enumerate(t):
        v,k = fun(k,v)
        index = k if k != 0 else 1 + len(u)
        u[index] = v
    return u

def sort(t,fun):
    return sorted(t, key = fun)

def keys(t):
    return sorted(kap(t,))