
import functools

data = open('6/data.txt', 'r')
fishStates = list(map(lambda x: (1,int(x)), data.readline().strip().split(',')))

LAST_DAY = 256
day = 1
while day <= LAST_DAY:
    newFishesStates = []
    nbNewFishes = 0
    for fish in fishStates:
        if fish[1] > 0:
            newFishesStates.append((fish[0], fish[1]-1))
        else:
            newFishesStates.append((fish[0], 6)) # 6 - timer value of a fish once it gives birth
            nbNewFishes += fish[0]
        
    if nbNewFishes > 0:
        newFishesStates.append((nbNewFishes,8))
   
    print("Day{}, Nb:{}".format(day, functools.reduce(lambda acc,fish: acc+fish[0], newFishesStates,0)))

    fishStates = newFishesStates
    day += 1
