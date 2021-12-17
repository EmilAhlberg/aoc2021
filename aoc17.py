t = open('input/17put.txt', 'r').readlines()[0]
xs = [int(xx) for xx in t.split('=')[1].split(',')[0].split('..')]
ys = [int(yy) for yy in  t.split('=')[2].strip().split('..')]

def p1():
    ans = (0,0)
    for y_force in range(500):
        y_max= y_force*(y_force+1) / 2
        for i in range(500): # only calculate desc part
            y_pos = y_max - i*(i+1) / 2
            if ys[0] <= y_pos <=ys[1]:
                ans=(y_force, y_max)
            elif y_pos < ys[0]: break
    return ans
y_max_force, y_max = p1()
#p2
answers = 0
for x_force in range(xs[1]+1):
    for y_force in range(ys[0], y_max_force+1):
        x = y = 0
        for step in range(0,500):
            x += max(x_force-step, 0)
            y += y_force-step
            if ys[0] <= y <= ys[1] and xs[0] <= x <= xs[1]: 
                answers += 1
                break
            elif x > xs[1] or y < ys[0] and y_force >=step: break
print(y_max, answers)



