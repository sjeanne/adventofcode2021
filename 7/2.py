import functools

data = open('7/data.txt', 'r')
crabPositions = list(map(int, data.readline().strip().split(',')))

furtherCrabPosition = functools.reduce(lambda acc, pos: pos if pos > acc else acc, crabPositions)

def fuelConsumption(startPos, endPos):
    # sum all interger from 1 to n = n * (n+1) / 2
    distance = abs(endPos - startPos)
    return distance * (distance + 1) / 2

bestPos = (0, 999999999999999) # (Position, fuel needed)
for pos in range(furtherCrabPosition):
    currentPosFuel = 0
    for crab in crabPositions:
        currentPosFuel += fuelConsumption(crab, pos)
    if currentPosFuel < bestPos[1]:
        bestPos = (pos, currentPosFuel)

print(bestPos)