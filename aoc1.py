nbrs = [int(s) for s in open('input/1put.txt', 'r')]
solver = lambda x: sum([1 for i in range(x,len(nbrs)) if nbrs[i-x] < nbrs[i]])
print(solver(1), solver(3))