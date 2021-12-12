import functools

def is_cave_small(cave):
    return cave == cave.lower()

def explore(cave_map, current_path, current_cave, founded):
    for cave in cave_map[current_cave]:
        path = list(current_path)
        if cave == "start":
            continue
        if cave == "end":
            path.append(cave)
            print(path)
            founded.append(path)
            continue
        if is_cave_small(cave) and cave in path:
            continue

        path.append(cave)
        explore(cave_map, path, cave,founded)
    

data = open('12/data.txt', 'r')
cave_map = {}

while True:
    line = data.readline().strip()
    if not line:
        break
    path = line.split('-')
    if len(path) != 2:
        break;
    (point1, point2) = path
    if not point1 in cave_map.keys():
        cave_map[point1] = []
    cave_map[point1].append(point2)
    if not point2 in cave_map.keys():
        cave_map[point2] = []
    cave_map[point2].append(point1)

founded = []
explore(cave_map, ["start"], "start",founded)
print(len(founded))