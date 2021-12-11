from functools import reduce

d = {"forward": lambda y: (y, 0), "down": lambda y: (0, y), "up": lambda y: (0, -y)}
data = [d[x](int(y)) for (x,y) in [s.split(' ') for s in open('input/2put.txt', 'r')]]
p1 = reduce(lambda x,y:x*y,[sum(i) for i in zip(*data)])

aim,p2 = 0, (0,0)
for (x,y) in data: # for loop :(
    aim += y
    p2 = (x + p2[0], p2[1] + aim*x)
print(p1, p2[0]*p2[1])