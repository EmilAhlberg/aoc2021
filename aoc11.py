M = [[int(ch) for ch in line.strip()] for line in open('input/11put.txt', 'r')]
p1, n,m, steps = 0, len(M), len(M[0]), 1000

def propagate(i,j):
    if i < 0 or j < 0 or i == n or j == n or (i,j) in flashIx: return
    M[i][j]+=1
    if M[i][j] <= 9: return
    flashIx.add((i,j))
    for ii in range(-1,2):
        for jj in range(-1,2):
            if ii == 0 and ii == jj: continue
            propagate(i+ii,j+jj)    
    

for step in range(1,steps):
    flashIx = set()
    for i in range(n):
        for j in range(m):
            if M[i][j] == 9: propagate(i,j)
            else: M[i][j]+=1
    if step <= 100: p1+= len(flashIx)
    elif n*m == len(flashIx): 
        print(p1, step)
        exit()
    for i,j in flashIx:
        M[i][j]=0