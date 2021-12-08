import functools

def findDigitMap(signalInput):
    digitsByChar = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],0:[]}
    digitsToLetter = {}
    for digit in signalInput:
        dig = list(digit)
        dig.sort()
        digitsByChar[len(digit)].append( dig)

    #Find 1 - 7(digit) - 1(digit)
    digitsToLetter[1] = list(set(digitsByChar[3][0]) - set(digitsByChar[2][0]))[0]

    #find 7
    for num in digitsByChar[6]:
        last = list(set(num) - set(digitsByChar[4][0] ) - set(digitsByChar[3][0] ))
        if len(last) == 1:
            digitsToLetter[7] = last[0]
            break

    #find 5
    for num in digitsByChar[6]:
        last = list(set(num) - set(digitsByChar[4][0] ) - set(digitsByChar[3][0]) - set(digitsToLetter[7]))
        if len(last) == 1:
            digitsToLetter[5] = last[0]
            break

    #find 2
    for num in digitsByChar[6]:
        last = list(set(num) - set(digitsByChar[3][0]) - set([digitsToLetter[7], digitsToLetter[5]]))
        if len(last) == 1:
            digitsToLetter[2] = last[0]
            break

    # find 4
    for num in digitsByChar[5]:
        last = list(set(num) - set(digitsByChar[3][0]) - set([digitsToLetter[7], digitsToLetter[5], digitsToLetter[2]]))
        if len(last) == 1:
            digitsToLetter[4] = last[0]
            break

    # find 6
    for num in digitsByChar[6]:
        last = list(set(num) - set([digitsToLetter[7], digitsToLetter[5], digitsToLetter[2],digitsToLetter[1], digitsToLetter[4]]))
        if len(last) == 1:
            digitsToLetter[6] = last[0]
            break

    # find 3
    digitsToLetter[3] = list(set(digitsByChar[7][0]) - set(digitsToLetter.values()))[0]

    return digitsToLetter

def computeDigit(mapSignalWire):
    return {
        1:{mapSignalWires[3], mapSignalWires[6]},
        2:{mapSignalWires[1],mapSignalWires[3],mapSignalWires[4],mapSignalWires[5],mapSignalWires[7]},
        3:{mapSignalWires[1],mapSignalWires[3],mapSignalWires[4],mapSignalWires[6],mapSignalWires[7]},
        4:{mapSignalWires[2],mapSignalWires[4],mapSignalWires[3],mapSignalWires[6]},
        5:{mapSignalWires[1],mapSignalWires[2],mapSignalWires[4],mapSignalWires[6],mapSignalWires[7]},
        6:{mapSignalWires[1],mapSignalWires[2],mapSignalWires[4],mapSignalWires[6],mapSignalWires[7],mapSignalWires[5]},
        7:{mapSignalWires[3], mapSignalWires[6],mapSignalWires[1]},
        8:{mapSignalWires[1],mapSignalWires[2],mapSignalWires[5],mapSignalWires[6],mapSignalWires[7],mapSignalWires[3],mapSignalWires[4]},
        9:{mapSignalWires[1],mapSignalWires[2],mapSignalWires[4],mapSignalWires[6],mapSignalWires[7],mapSignalWires[3]},
        0:{mapSignalWires[1],mapSignalWires[2],mapSignalWires[5],mapSignalWires[6],mapSignalWires[7],mapSignalWires[3]},
    }

def DigitToNum(signal, remapDigit):
    for num in remapDigit.keys():
        digit = remapDigit[num]
        if digit == set(list(signal)):
            return num

data = open('8/data.txt', 'r')
signals = []
while True:
    line = data.readline()
    if not line:
        break
    signal = list(map(lambda x: x.strip().split(), line.strip().split('|')))
    signals.append((signal[0], signal[1]))


outputSum = 0

for digitSignal in signals:
    mapSignalWires = findDigitMap(digitSignal[0])
    remapDigit = computeDigit(mapSignalWires)

    n = 3
    number = 0
    for signal in digitSignal[1]:
        num = DigitToNum(signal, remapDigit)
        number += num * pow(10,n)
        n -= 1
    print( number)
    outputSum += number

print("Final:", outputSum)