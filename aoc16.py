from functools import reduce

def pHelp(pos, b, offset):
    return pos+offset, int(b[pos:pos+offset],2)

def parsePacket(pos):
    values, subPacketLength = [],0
    pos, version = pHelp(pos,b,3)
    pos,packetType = pHelp(pos,b,3)
    if packetType == 4:
        bigEndianDecimals,isParsingLiteral = [],True
        while isParsingLiteral:
            if b[pos] == '0': isParsingLiteral = False
            bigEndianDecimals.append(int(b[pos+1:pos+5],2))
            pos+=5
        val=0
        for i, dec in enumerate(bigEndianDecimals): val += dec << 4*(len(bigEndianDecimals)-1-i)
        values.append(val)
    else:
        pos, lengthTypeID = pHelp(pos,b,1)
        bits = 11 if lengthTypeID == 1 else 15
        pos,subPacketLength = pHelp(pos,b,bits)
        if lengthTypeID == 1:        
            for packetNbr in range(subPacketLength): 
                pos, v, versionTerm = parsePacket(pos)
                values.append(v)
                version+=versionTerm
        else:
            while subPacketLength > 3:
                newPos, v, versionTerm = parsePacket(pos)
                values.append(v)
                version+=versionTerm
                subPacketLength -= (newPos-pos)
                pos=newPos
    return pos, dF[packetType](values), version

        

dF = {0: lambda X: reduce(lambda x,y: x+y, X), 1: lambda X: reduce(lambda x,y: x*y, X,1), 2: lambda X: min(X), 3: lambda X: max(X), 
    4: lambda X: X[0],5: lambda X: 1 if X[0]>X[1] else 0, 6: lambda X: 1 if X[0]<X[1] else 0, 7: lambda X: 1 if X[0] == X[1] else 0}
data = open('input/16put.txt','r').readlines()[0]
b = str(format(int(data,16),'0{}b'.format(len(data)*4)))
print(parsePacket(0))
