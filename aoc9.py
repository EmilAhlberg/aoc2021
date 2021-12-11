from functools import reduce
M = [[int(nbr) for nbr in line.strip()] for line in open('input/9put.txt', 'r') ]
def p1():
    p1, lp = 0, []
    for i,row in enumerate(M):
        for j, v in enumerate(row):
            u = M[i-1][j] > v if i > 0 else True
            d = M[i+1][j] > v if i < len(M)-1 else True
            l = M[i][j-1] > v if j > 0 else True
            r = M[i][j+1] > v if j < len(M[0])-1 else True
            if u and d and l and r:
                p1 += v+1
                lp.append((i,j)) #p2 prep
    return p1, lp

def p2():
    def rec(i,j):
        if i < 0 or j < 0 or i == len(M) or j == len(M[0]) or M[i][j] == 9: return 0
        v = M[i][j]
        M[i][j] = 9
        u = rec(i-1, j) if i > 0 and M[i-1][j] >= v else 0
        d = rec(i+1, j) if i < len(M)-1 and M[i+1][j] >= v else 0
        l = rec(i, j-1) if j > 0 and M[i][j-1] >= v else 0
        r = rec(i, j+1) if j < len(M[0])-1 and M[i][j+1] >= v else 0
        return 1 + u + d + l + r
    return reduce(lambda x,y: x*y,sorted(list(map(lambda t: rec(t[0], t[1]), lp)))[-3:]) # :)
p1, lp = p1()
print(p1, p2())