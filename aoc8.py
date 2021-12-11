def charXor(s1,s2):
    for c in s1: 
        if c not in s2: return c
    return ''

t = [(y.strip().split() for y in x) for x in  [line.split('|') for line in open('input/8put.txt', 'r') ]]
easyMap, p1, p2 = {2: 1, 3: 7, 4:4, 7:8}, 0, 0
for (digits,row) in t:
    l = sorted(digits, key=lambda x: len(x))
    pos3 = -1
    for i in range(6,9):
        fourZeroDiff = charXor(l[2], l[i])
        if fourZeroDiff != '' and charXor(l[0], l[i]) == '':
            pos3 = fourZeroDiff
            break        
    pos0 = charXor(l[2], l[0]+ pos3)
    for i, output in enumerate(row):
        t, n = 0,len(output)
        if n in easyMap:
            p1+=1
            t = easyMap[n]
        elif n == 5:
            if pos0 in output: t = 5
            elif charXor(l[0], output) == '': t = 3
            else: t = 2
        else:
            if not pos3 in output: t =  0
            elif charXor(l[0], output) == '' in output: t = 9
            else: t = 6
        p2 += t * 10**(3-i)
print(p1, p2)