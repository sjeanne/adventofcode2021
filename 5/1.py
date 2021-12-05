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
    # keep only H/V vents
    print(vent)
    if vent[X1] == vent[X2]:
        for y in range(min(vent[Y1],vent[Y2]), max(vent[Y1],vent[Y2])+1):
            map[(vent[X2],y)] = map.get((vent[X2],y), 0) + 1
    elif vent[Y1] == vent[Y2]:
        for x in range(min(vent[X1],vent[X2]), max(vent[X1],vent[X2])+1):
            map[(x,vent[Y2])] = map.get((x,vent[Y2]), 0) + 1
    else:
        #Not vertical or Horizon vent
        pass

count = len(list(filter(lambda x: x > 1, map.values())))

print("Count:", count)