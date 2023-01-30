import math
import Constants
import io
import re

const = Constants.Constants()
seed = const.seed


# Utility functions for numerics
def rint(lo,hi):
    return math.floor(0.5 + rand(lo,hi))


def rand(lo=0,hi=1):
    """
    This function generates the random number between a given range
    """
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
    s = str(s)
    def fun(s1):
        s1 = s1.lower()
        print(s1)
        if s1 == "true":
            return True
        elif s1 == "false":
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


def csv(filename: str, fun):
    f = io.open(filename)
    while True:
        s = f.read()
        if s:
            t = []
            for s1 in re.findall("([^,]+)" ,s):
                t.append(coerce(s1))
            fun(t)
        else:
            return f.close()