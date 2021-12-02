# Using readline()
data = open('data.txt', 'r')
count = 0

previousDepth = 10000000
increasedDepth = 0
while True:
    count += 1
 
    # Get next line from file
    line = data.readline()
 
    if not line:
        break
    currentDepth = int(line.strip())
    depthHasIncreased = currentDepth > previousDepth
    previousDepth = currentDepth
    print("Line{}: {} - {}".format(count, currentDepth, depthHasIncreased))
    if(depthHasIncreased):
        increasedDepth += 1
    previousDepth = currentDepth

print("# increasedDepth: {}".format(increasedDepth))
data.close()