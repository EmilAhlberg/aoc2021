crabs = [int(crab) for line in open('input/7put.txt', 'r') for crab in line.split(',')]
p1 = p2 = 999999999999 # big boy
for nbr in crabs:
    s1 = s2 = 0
    for pos in crabs:
        dist = abs(nbr-pos)
        s1 += dist
        s2 += dist*(dist+1) / 2
    p1,p2 = min(p1, s1),min(p2, s2)
print(p1Answer, int(p2Answer))