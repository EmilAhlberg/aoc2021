#maybe threw away p1 solver here? (trivial problem) 
RB,n = [0]*9, 9
for line in open('input/6put.txt', 'r'): 
    for nbr in line.split(','): RB[int(nbr)] += 1
for i in range(256): RB[(i + 7) % n] += RB[i%n] #1337
print(sum(RB))
