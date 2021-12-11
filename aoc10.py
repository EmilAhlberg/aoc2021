mp1 = {')': ('(', 3), ']': ('[', 57), '}': ('{',1197), '>': ('<', 25137)}
mp2 = {'(': 1, '[': 2, '{': 3, '<': 4}
p1,p2 = 0, [],
for line in [ s.strip() for s in open('input/10put.txt', 'r')]:
    stack, corrupted = [], False
    for ch in line:
        if ch not in mp1: stack.append(ch)
        elif mp1[ch][0] != stack.pop(): 
            p1+=mp1[ch][1] 
            corrupted=True
            break
    if not corrupted:
        p2.append(0)
        while len(stack): p2[-1] += p2[-1]*5 + mp2[stack.pop()]

print(p1, sorted(p2)[len(p2)//2])