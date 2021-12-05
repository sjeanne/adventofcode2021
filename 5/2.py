import re

# Constants
X1 = 0
Y1 = 1
X2 = 2
Y2 = 3

def parseInputLine(line):
    pattern = re.compile('(\d+),(\d+) -> (\d+),(\d+)')
    matched = pattern.match(line)
    return list(map(int,[matched.group(1),matched.group(2),matched.group(3),matched.group(4)]))

 # load data
data = open('5/data.txt', 'r')
vents = []
while True:
    line = data.readline().strip()
    if not line:
        break
    vents.append(parseInputLine(line))

map = {}
for vent in vents:
    if vent[X1] == vent[X2]:
        for y in range(min(vent[Y1],vent[Y2]), max(vent[Y1],vent[Y2])+1):
            map[(vent[X2],y)] = map.get((vent[X2],y), 0) + 1
    elif vent[Y1] == vent[Y2]:
        for x in range(min(vent[X1],vent[X2]), max(vent[X1],vent[X2])+1):
            map[(x,vent[Y2])] = map.get((x,vent[Y2]), 0) + 1
    else:
        leftPoint = (vent[X1], vent[Y1]) if vent[X1] < vent[X2] else (vent[X2], vent[Y2])
        rightPoint = (vent[X1], vent[Y1]) if vent[X1] > vent[X2] else (vent[X2], vent[Y2])
        print("L:", leftPoint, "R:", rightPoint)
        yDelta = -1 if rightPoint[1] < leftPoint[1] else 1
        for x in range(rightPoint[0] - leftPoint[0] + 1):
            print(leftPoint[0]+x, leftPoint[1]+x*yDelta)
            map[(leftPoint[0]+x, leftPoint[1]+x*yDelta)] = map.get((leftPoint[0]+x, leftPoint[1]+x*yDelta),0) + 1

count = len(list(filter(lambda x: x > 1, map.values())))

print("Count:", count)