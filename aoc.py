from functools import reduce

def a1():
    nbrs = [int(s) for s in open('1put.txt', 'r')]
    solver = lambda x: sum([1 for i in range(x,len(nbrs)) if nbrs[i-x] < nbrs[i]])
    return solver(1), solver(3)

def a2():
    d = {"forward": lambda y: (y, 0), "down": lambda y: (0, y), "up": lambda y: (0, -y)}
    data = [d[x](int(y)) for (x,y) in [s.split(' ') for s in open('2put.txt', 'r')]]
    p1 = reduce(lambda x,y:x*y,[sum(i) for i in zip(*data)])
    
    aim,p2 = 0, (0,0)
    for (x,y) in data: # for loop :(
        aim += y
        p2 = (x + p2[0], p2[1] + aim*x)
    return p1, p2[0]*p2[1]

def a3():
    lines = [[int(bit) for bit in line.strip()] for line in open('3put.txt', 'r')]
    ewBitSum = lambda lines: list(map(lambda bitSum: int(bitSum >= len(lines)/2), [sum(line) for line in zip(*lines)]))
    bitFlipper = lambda bits: list(map(lambda x: int(not x), bits))
    bitsToDecimal = lambda bits: reduce(lambda  acc, ixBit: acc+ (ixBit[1] << (len(bits)-1-ixBit[0])),enumerate(bits), 0) 
    gamma = ewBitSum(lines)
    epsilon = bitFlipper(gamma)
    p1 = bitsToDecimal(gamma)*bitsToDecimal(epsilon)

    o2, co2, pos = set(list(range(0,len(lines)))), set(list(range(0,len(lines)))), 0
    while len(o2) > 1 or len(co2) > 1:
        if len(o2) > 1:
            o2s = ewBitSum([lines[i] for i in o2])
            o2 = set([ix for ix in o2 if lines[ix][pos] == o2s[pos]])
        if len(co2) > 1:
            co2s = bitFlipper(ewBitSum([lines[i] for i in co2]))
            co2 = set([ix for ix in co2 if lines[ix][pos] == co2s[pos]])
        pos += 1
    p2Solver = lambda ix: bitsToDecimal(lines[ix])
    return p1, p2Solver(o2.pop())*p2Solver(co2.pop())

def a4():
    def setup():
        with open('4put.txt','r') as f:
            lookup, lines = dict(), f.readlines()
            nbrs, n, step = [int(nbr) for nbr in lines[0].split(',')], len(lines), 6
            mxs = [[] for _ in range(n // step)]
            for i in range(0, n // step ):
                for j in range(1, step):
                    mxs[i].append([])
                    mxs[i][j-1] = [int(nbr) for nbr in lines[i*step+1+j].split()]
                    for k, nbr in enumerate(mxs[i][j-1]):
                        t = (i,j-1,k)
                        if nbr not in lookup: lookup[nbr]= [t]
                        else: lookup[nbr].append(t)
        return lookup, mxs, nbrs

    def findWinner(isP1):
        bingo, mx, wonMxs = -1, -1, {-1}
        for ix, nbr in enumerate(nbrs):
            if bingo != -1 and isP1: break
            for (i,j,k) in lookup[nbr]:
                if i in wonMxs: continue
                mxs[i][j][k] = -1
                if ix >= 4:
                    for jj in range(5):
                        if mxs[i][jj][k] != -1: break 
                        if jj == 4: 
                            bingo, mx = nbr, mxs[i]
                            wonMxs.add(i)
                    for kk in range(5):
                        if mxs[i][j][kk] != -1: break 
                        if kk == 4: 
                            bingo, mx = nbr, mxs[i]
                            wonMxs.add(i)
        return bingo * sum([nbr for row in mx for nbr in row if nbr != -1])   
        
    lookup, mxs, nbrs = setup() # lookup: wroom wroom
    return findWinner(True), findWinner(False)


def a5():
    nbrs = [x for line in open('5put.txt', 'r') for x in line.replace(',', ' ').split() if x != '->']
    coords = [(int(nbrs[0+i]),int(nbrs[1+i]),int(nbrs[2+i]),int(nbrs[3+i])) for i in range(0,len(nbrs), 4)]
    gridSize = 1000
    M = [[0 for i in range(gridSize)] for j in range(gridSize)]
    for (x1,y1,x2,y2) in coords:
        if x1 == x2:
            mx,mn = max(y1,y2),min(y1,y2)
            for i in range(mn,mx+1): M[x1][i] += 1
        elif y1 == y2:
            mx,mn = max(x1,x2), min(x1,x2)
            for i in range(mn,mx+1): M[i][y1] += 1
        else:
            dx, dy = x1-x2, y1-y2
            for offset in range(abs(dx)+1):
                if dx < 0:
                    if dy < 0: M[x1+offset][y1+offset] += 1
                    else: M[x1+offset][y1-offset] += 1
                else:
                    if dy < 0: M[x1-offset][y1+offset] += 1
                    else: M[x1-offset][y1-offset] += 1
    p1or2 = sum([1 for row in M for pos in row if pos > 1])
    return p1or2

def a6():
    n=9
    RB = [0]*n
    for line in open('6put.txt', 'r'):
        for nbr in line.split(','): RB[int(nbr)] += 1
    for i in range(256): RB[(i + 7) % n] += RB[i%n] #1337
    return sum(RB)

def a7():
    crabs = [int(crab) for line in open('7put.txt', 'r') for crab in line.split(',')]
    p1Answer = p2Answer = 999999999999 # big boy
    for nbr in crabs:
        p1 = p2 = 0
        for pos in crabs:
            dist = abs(nbr-pos)
            p1 += dist
            p2 += dist*(dist+1) / 2
        p1Answer = min(p1Answer, p1)
        p2Answer = min(p2Answer, p2)
    return p1Answer, int(p2Answer)
    