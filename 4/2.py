
import functools

def parseBingoTable(data):
    grid = []
    for i in range(5):
        grid.extend( list(map(int,data.readline().strip().split())))
    return grid

def extractLineN(grid, line):
    return [grid[(line*5)],
                grid[(line*5)+1],
                grid[(line*5)+2],
                grid[(line*5)+3],
                grid[(line*5)+4]]

def extractColN(grid, col):
    return [grid[(col)],
                grid[(col+5)],
                grid[(col+10)],
                grid[(col+15)],
                grid[(col+20)]]

def isGridWinning(grid, numbersDrawn):
    # row
    for i in range(5):
        line = extractLineN(grid, i)
        if( line[0] in numbersDrawn
        and line[1] in numbersDrawn
        and line[2] in numbersDrawn
        and line[3] in numbersDrawn
        and line[4] in numbersDrawn):
            return line
    
    # column
    for i in range(5):
        col = extractColN(grid, i)
        if(col[0] in numbersDrawn
        and col[1] in numbersDrawn
        and col[2] in numbersDrawn
        and col[3] in numbersDrawn
        and col[4] in numbersDrawn):
            return col
    return []

def filterList(list, val):
    output = []
    for i in list:
        if not (i in val):
            output.append(i)
    return output

# Load data
data = open('4/data.txt', 'r')
pickedNumbers = list(map(int,data.readline().strip().split(',')))

grids = []
while True:
    line = data.readline()
    if not line:
        break
    grids.append(parseBingoTable(data))

data.close()

# Play BINGO !!!
isWinnerFound = False
drawnNumber = 5
while len(grids) > 0:
    for grid in grids:
        result = isGridWinning(grid, pickedNumbers[0:drawnNumber+1])
        if len(result) > 0:
            isWinnerFound = True
            filteredGrid = filterList(grid,pickedNumbers[0:drawnNumber+1])
            lastPiced = pickedNumbers[drawnNumber]
            sum = functools.reduce( lambda x,y: x+y, filteredGrid)
            print("G:{}, L:{}, R:{}".format(grid, lastPiced, sum * lastPiced ))
            grids.remove(grid)
    drawnNumber +=1
    
    
    
        
