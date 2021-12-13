coords = [(line.strip().split(',')[0],line.strip().split(',')[1]) for line in open('input/13put_1.txt', 'r')]
coords = [(int(x),int(y)) for x,y in coords] #would be nice as a set from start
folds = [(x.split('=')[0], int(x.split('=')[1])) for x in  [line.strip().split()[-1] for line in open('input/13put_2.txt', 'r')]]

#orientation,pivot = folds[0][0], folds[0][1] #p1
for orientation, pivot in folds:
    for j,coord in enumerate(coords): 
        if orientation == "x" and coord[0] > pivot: coords[j] = (2*pivot - coord[0],coord[1])
        elif orientation == "y" and coord[1] > pivot: coords[j] = (coord[0],2*pivot-coord[1])

M = [[0]*40 for i in range(8)]
print(len(set(coords)))#p1 unique points
for i,j in coords: M[j][i] = 4
for row in M:print(''.join(str(row)).replace('0',' ').replace(',',' '))



