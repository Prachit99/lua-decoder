import math
import Constants
import io
import copy
import re
import json
from Sym import SYM

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


def o(t):
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


def repCols(cols, data):
    cols = copy.deepcopy(cols)
    for col in cols:
        col[len(col)-1] = col[0] + ":" + col[len(col)-1]
        for j in range(1, len(col)):
            col[j-1] = col[j]
        col.pop()
    col_1 = ['Num' + str(k+1) for k in range(len(cols[1])-1)]
    col_1.append('thingX')
    cols.insert(0, col_1)
    return data(cols)


def repRows(t, data, rows):
    rows = copy.deepcopy(rows)
    for j,s in enumerate(rows[-1]):
        rows[0][j] += ":" + s
    rows.pop()
    for n,row in enumerate(rows):
        if n == 0:
            row.append('thingX')
        else:
            u = t['rows'][-n]
            row.append(u[len(u)-1])
    return data(rows)


def doFile(file):
    file = open(file, 'r', encoding='utf-8')
    #print(re.findall(r'(?<=return )[^.]*', file.read())[0])
    text  = re.findall(r'(?<=return )[^.]*', file.read())[0].replace('{', '[').replace('}',']').replace('=',':').replace('[\n','{\n' ).replace(' ]',' }' ).replace('\'', '"').replace('_', '"_"')
    print(text)
    file.close()
    return json.loads(re.sub("(\w+):", r'"\1":', text))


def transpose(t):
    u=[]
    for i in range(len(t[1])):
        u.append([])
        for j in range(len(t)):
            u[i].append(t[j][i])
    return u


def repPlace(data):
    n,g = 20,{}
    for i in range(1, n+1):
        g[i] = {}
        for j in range(1, n+1):
            g[i][j] = ' '
    y_max = 0
    print('')
    for r,row in enumerate(data.rows):
        print((data.rows))
        c = chr(97+r).upper()
        print(row)
        print(c, row.cells[-1])
        x,y = row.x*n//1, row.y*n//1
        y_max = int(max(y_max,y+1))
        g[y+1][x+1] = c
    print('')
    for y in range(1,y_max+1):
        print(' '.join(g[y].values()))


def repgrid(file, data):
    t = doFile(file)
    rows = repRows(t, data, transpose(t['cols']))
    cols = repCols(t['cols'], data)
    show(rows.cluster(),"mid",rows.cols.all,1)
    show(cols.cluster(),"mid",cols.cols.all,1)
    repPlace(rows)


def RANGE(at,txt,lo,hi=None):
    return {'at':at,'txt':txt,'lo':lo,'hi':lo or hi or lo,'y':SYM()}


def extend(range, n, s):
    range['lo'] = min(n, range['lo'])
    range['hi'] = max(n, range['hi'])
    range['y'].add(s)


def merge(col1, col2):
  new = copy.deepcopy(col1)
  if isinstance(col1, SYM):
      for n in col2.has:
        new.add(n)
  else:
    for n in col2.has:
        new.add(new, n)
    new.lo = min(col1.lo, col2.lo)
    new.hi = max(col1.hi, col2.hi) 
  return new


def merge2(col1, col2):
  new = merge(col1, col2)
  if new.div() <= (col1.div()*col1.n + col2.div()*col2.n)/new.n:
    return new
  

def mergeAny(ranges0):
    def noGaps(t):
        for j in range(1, len(t)):
            t[j]['lo'] = t[j - 1]['hi']
        t[0]['lo']  = -float("inf")
        t[len(t) - 1]['hi'] =  float("inf")
        return t

    ranges1 = []
    j = 0
    while j <= len(ranges0) - 1:
        left = ranges0[j]

        if j == len(ranges0)-1:
            right = None
        else: 
            right = ranges0[j+1]

        if right:
            y = merge2(left['y'], right['y'])
            if y:
                j = j+1
                left['hi'], left['y'] = right['hi'], y
        ranges1.append(left)
        j = j+1

    if len(ranges0) == len(ranges1):
        return noGaps(ranges0)
    else: 
        return mergeAny(ranges1)
    

def bins(cols, rowss):
    out = []
    for col in cols:
        ranges = {}
        for y,rows in rowss.items():
            for row in rows:
                x = row.cells[col.at]
                if x != "?":
                    k = int(bin(col, x))
                    if not k in ranges:
                        ranges[k] = RANGE(col.at, col.txt, x)
                    extend(ranges[k], x, y)
        ranges = list(dict(sorted(ranges.items())).values())
        r = ranges if isinstance(col, SYM) else mergeAny(ranges)
        out.append(r)
    return out


def bin(col, x):
    if x=="?" or isinstance(col, SYM):
        return x
    tmp = (col.hi - col.lo)/(Constants().bins - 1)
    return  1 if col.hi == col.lo else math.floor(x/tmp + .5)*tmp
