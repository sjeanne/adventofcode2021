import functools
from operator import itemgetter

def found_low_spot(cave_map, cave_size):
    low_points = []
    for pos in range(len(cave_map)):
        map_width = cave_size[0]
        if pos % map_width == map_width-1:
            possible_indices = [pos-1, pos+map_width, pos-map_width]
        elif pos % map_width == 0:
            possible_indices = [pos+1, pos+map_width, pos-map_width]
        else:
            possible_indices= [pos-1, pos+1, pos+map_width, pos-map_width]
        indices = list(filter(lambda x:  x >=0 and x < cave_size[0]*cave_size[1], possible_indices))
        lowest_neightboor = functools.reduce(lambda x,y: x if x < y else y, list((itemgetter(*indices)(cave_map))))
        if cave_map[pos] < lowest_neightboor:
            low_points.append((pos,cave_map[pos]))
    return low_points

def explore_bassins(cave_map, cave_size, bassin):
    pos = bassin[-1][0]
    map_width = cave_size[0]
    if pos % map_width == map_width-1:
        possible_indices = [pos-1, pos+map_width, pos-map_width]
    elif pos % map_width == 0:
        possible_indices = [pos+1, pos+map_width, pos-map_width]
    else:
        possible_indices= [pos-1, pos+1, pos+map_width, pos-map_width]
    indices = list(filter(lambda x:  x >=0 and x < cave_size[0]*cave_size[1], possible_indices))

    for point in indices:
        if cave_map[point] < 9 and not (point,cave_map[point]) in bassin:
            bassin.append((point,cave_map[point]))
            bassin = explore_bassins(cave_map,cave_size,bassin)
    return bassin

def find_bassins(cave_map, cave_size, low_points):
    bassins = []
    for low_point in low_points:
        bassin = explore_bassins(cave_map, cave_size, [low_point])
        bassins.append(bassin)
    return bassins


data = open('9/data.txt', 'r')

cave_map = []
cave_size = (0,0)
while True:
    line = data.readline().strip()
    if not line:
        break
    cave_map.extend(list(map(int,list(line))))
    cave_size = (len(line),cave_size[1] + 1)

low_points = found_low_spot(cave_map, cave_size)
print(low_points)
bassins = find_bassins(cave_map,cave_size,low_points)
print(bassins)
sizes = list(map(lambda x: len(x), bassins))
sizes.sort()
print(sizes)
print(functools.reduce(lambda acc,x: acc * x, sizes[-3:]))