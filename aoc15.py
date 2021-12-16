from queue import PriorityQueue
M = [[int(i) for i in line.strip()] for line in open('input/15put.txt', 'r')]
n,m = len(M), len(M[0])
R=[[2**63 - 1 for nbr in row] for row in M]
R[0][0] = 0

def djikstra():
    visited = set()
    q = PriorityQueue()
    q.put((0, (0,0)))
    while not q.empty():
        (risk, node) = q.get() 
        visited.add(node)
        i,j = node
        edges = []
        if i < n-1: edges.append((i+1,j))
        if j < m-1: edges.append((i,j+1))
        if i > 0: edges.append((i-1,j))
        if j > 0: edges.append((i,j-1))
        for ii,jj in edges:
            newRisk = R[i][j] + M[i][j]
            if (ii,jj) not in visited and R[ii][jj] > newRisk:
                q.put((newRisk, (ii,jj)))
                R[ii][jj] = newRisk

djikstra()
print(R[-1][-1])
oldM = M
M =[[0]*5*m for i in range(5*n)] 
for i in range(5):
    for j in range(5):
        for ii in range(n):
            for jj in range(m):
                M[n*i+ii][m*j+jj] = (oldM[ii][jj] + (i+j)) % 10 + 1

R=[[2**63 - 1 for nbr in row] for row in M]
R[0][0] = 0
n,m = len(M), len(M[0])
djikstra()
print(R[-1][-1])