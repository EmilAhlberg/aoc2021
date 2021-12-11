from functools import reduce
lines = [[int(bit) for bit in line.strip()] for line in open('input/3put.txt', 'r')]
ewBitSum = lambda lines: list(map(lambda bitSum: int(bitSum >= len(lines)/2), [sum(line) for line in zip(*lines)]))
bitFlipper = lambda bits: list(map(lambda x: int(not x), bits))
bitsToDecimal = lambda bits: reduce(lambda  acc, ixBit: acc+ (ixBit[1] << (len(bits)-1-ixBit[0])),enumerate(bits), 0) 
gamma = ewBitSum(lines)
epsilon = bitFlipper(gamma)
p1 = bitsToDecimal(gamma)*bitsToDecimal(epsilon)

o2, co2, pos = set(list(range(0,len(lines)))), set(list(range(0,len(lines)))), 0
while len(o2) > 1 or len(co2) > 1:
    if len(o2) > 1:
        o2s = ewBitSum([lines[i] for i in o2])
        o2 = set([ix for ix in o2 if lines[ix][pos] == o2s[pos]])
    if len(co2) > 1:
        co2s = bitFlipper(ewBitSum([lines[i] for i in co2]))
        co2 = set([ix for ix in co2 if lines[ix][pos] == co2s[pos]])
    pos += 1
p2Solver = lambda ix: bitsToDecimal(lines[ix])
print(p1, p2Solver(o2.pop())*p2Solver(co2.pop()))