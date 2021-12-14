class Node:
    def __init__(self, val,next=None):
        self.val= val
        self.next = next

i = [x for x in open('input/14put.txt','r')]
template, rules = i[0].strip(), {line.strip().split(' -> ')[0]:line.strip().split(' -> ')[1] for line in i[2:]}
#P1 - linked list
node = dummyNode =  Node('')
for ch in template: 
    node.next = Node(ch)
    node = node.next
for step in range(10):
    node = dummyNode.next
    while node.next:
        newNode = Node(rules[node.val + node.next.val], node.next)
        node.next=newNode
        node=newNode.next
result, m, node = '', {}, dummyNode.next
while node:
    if node.val not in m: m[node.val]=1
    else: m[node.val]+=1
    result += node.val
    node = node.next
p1 =  m[max(m, key=m.get)] -  m[min(m, key=m.get)]
print(p1)
#P2 - 'pair map generation'
M = {}
for i in range(len(template)-1):
    pair = ''.join(template[i:i+2])
    if pair not in M: M[pair]=1
    else: M[pair]+=1
for step in range(40):
    newM = {}
    for k in M:
        for pair in [k[0] + rules[k], rules[k] + k[1]]:
            if pair not in newM: newM[pair]=M[k]
            else: newM[pair]+=M[k]
    M = newM
ans = {}
for ch1,ch2 in M:
    if ch1 not in ans: ans[ch1]=M[ch1+ch2]
    else: ans[ch1]+=M[ch1+ch2]
    if ch2 not in ans: ans[ch2]=M[ch1+ch2]
    else: ans[ch2]+=M[ch1+ch2]
p2 =  ans[max(ans, key=ans.get)] -  ans[min(ans, key=ans.get)] 
print((p2+1) // 2)
