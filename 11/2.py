import functools

def print_map(fishes_map, label):
    if label:
        print(label,":")
    for i in range(10):
        print(fishes_map[i*10:(i+1)*10])

def count_flash(fishes_map, pos):
    if pos % 10 == 9:
        possible_indices = [pos-1, pos+9, pos+10,  pos-11, pos-10]
    elif pos % 10 == 0:
        possible_indices = [pos+1, pos+10, pos+11, pos-10, pos-9]
    else:
        possible_indices= [pos-1, pos+1, pos+9, pos+10, pos+11, pos-11, pos-10, pos-9]
    indices = filter(lambda x:  x >=0 and x <= 99, possible_indices)
    nb_flash = 0
    for ind in indices: nb_flash += 1 if fishes_map[ind] == 0 else 0
    return nb_flash

def step_flash(fishes_map):
    fishes_map = list(map(lambda x: x+1 if x < 9 else 0, fishes_map))
    flashes = fishes_map.count(0)
    
    while 0 in fishes_map:
        for i in range(100):
            if fishes_map[i] > 0:
                fishes_map[i] += count_flash(fishes_map,i)
        fishes_map = list(map(lambda x: x if x > 0 else -1, fishes_map))
        fishes_map = list(map(lambda x: x if x <= 9 else 0, fishes_map))
        flashes += fishes_map.count(0)
    fishes_map = list(map(lambda x: x if x > 0 else 0, fishes_map))
    return (fishes_map, flashes)

data = open('11/data.txt', 'r')
fishes_map = []
while True:
    line = data.readline().strip()
    if not line:
        break
    fishes_map.extend(list(map(int,list(line))))

nb_steps = 0
while fishes_map.count(0) != 100:
    (fishes_map, nb_flashes) = step_flash(fishes_map)
    nb_steps += 1
print("Steps:",nb_steps)
