
data = open('6/data.txt', 'r')
fishStates = list(map(int, data.readline().strip().split(',')))

LAST_DAY = 80
day = 1
while day <= LAST_DAY:
    newFishesStates = []
    nbNewFishes = 0
    for fish in fishStates:
        if fish > 0:
            newFishesStates.append(fish-1)
        else:
            newFishesStates.append(6) # 6 - timer value of a fish once it gives birth
            nbNewFishes += 1
    if nbNewFishes > 0:
        newFishesStates.extend([8] * nbNewFishes)
    
    print("Day{}, Nb:{}: {}".format(day, len(newFishesStates)))

    fishStates = newFishesStates
    day += 1
