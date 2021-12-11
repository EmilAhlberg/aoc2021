def setup():
    with open('input/4put.txt','r') as f:
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
print(findWinner(True), findWinner(False))