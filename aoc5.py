nbrs = [x for line in open('input/5put.txt', 'r') for x in line.replace(',', ' ').split() if x != '->']
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
print(p1or2) #maybe threw away p1 solver here? hmm 