import math
import Constants
import io
import re

const = Constants.Constants()
seed = const.seed


# Utility functions for numerics
def rint(lo, hi):
    return math.floor(0.5 + rand(lo,hi))


def rand(lo=0, hi=1):
    """
    This function generates the random number between a given range
    """
    global seed
    seed = (16807 * seed) % 2147483647
    return lo + (hi - lo) * seed / 2147483647


def rnd(n, nPlaces=3):
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
    s = str(s)
    def fun(s1):
        if s1.lower() == "true":
            return True
        elif s1.lower() == "false":
            return False
        else:
            return s1
    s = fun(s)
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return fun(s)
    except Exception as exception:
        print("Coerce Error", exception)


# Utility functions for Lists
# def map(t,fun):
    # u = []
    # for k,v in enumerate(t):
    #     v,k = fun(k)
    #     index = k if k != 0 else 1+len(u)
    #     u[index] = v
    # return u


def kap(t, fun):
    u = {}
    for k,v in enumerate(t):
        # print(k, v.txt)
        v,k = fun(k,v)
        index = k if k != 0 else 1 + len(u)
        u[index] = v
    # print(u)
    return u


def sort(t, fun):
    return sorted(t, key = fun)


def keys(t):
    return sorted(kap(t,))


def csv(filename: str, fun):
    file = io.open(filename)
    t = []
    for line in file.readlines():
        row = list(map(coerce, line.strip().split(',')))
        t.append(row)
        fun(row)
    file.close()


def show(node, what, cols, nPlaces, lvl = 0):
  if node:
    print('| ' * lvl + str(len(node['data'].rows)) + '  ', end = '')
    if not node.get('left') or lvl==0:
        print(node['data'].stats("mid",node['data'].cols.y,nPlaces))
    else:
        print('')
    show(node.get('left'), what,cols, nPlaces, lvl+1)
    show(node.get('right'), what,cols,nPlaces, lvl+1)


def many(t,n):
    u=[]
    for r in range(1,n+1):
        u.append(any(t))
    return u


def any(t):
    return t[rint(0, len(t) - 1)]


def cosine(a,b,c):
    if c==0:
        d=1
    else:
        d=2*c
    x1 = (a**2 + c**2 - b**2) / d
    x2 = max(0, min(1, x1))
    y  = abs((a**2 - x2**2))**.5
    return x2, y
