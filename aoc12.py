class EmilNode:
    def __init__(self, e, name):
        self.history= set()
        self.edges = set([e])
        self.name = name

def setup():
    AM, edges = {}, [line.strip().split('-') for line in open('input/12put.txt', 'r')]
    for a,b in edges:
        if a not in AM: AM[a] = EmilNode(b, a)
        else: AM[a].edges.add(b)
        if b not in AM and a: AM[b] = EmilNode(a, b)
        else: AM[b].edges.add(a)
    return AM, set(), edges

def traverse(node, path, doubleDip):
    if doubleDip == 'start': return
    if path in node.history and doubleDip in ['', 'spent DD']: return
    node.history.add(path)
    if node.name == 'end': 
        ans.add(path)
        return
    for e in node.edges:
        if ord(e[0]) >= ord('a') and (e in path and e != doubleDip): continue # tuple -> set, possible optimization.. 
        if doubleDip == e: traverse(AM[e], path + (e,), 'spent DD')
        else: traverse(AM[e], path + (e,), doubleDip)
        if doubleDip == '': traverse(AM[e], path + (e,), e)

AM, ans, edges = setup()
traverse(AM['start'], ('start',), 'NO DOUBLE DIP')
p1 = len(ans)
AM, ans, edges = setup()
traverse(AM['start'], ('start',), '')
print(p1, len(ans))