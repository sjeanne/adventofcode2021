# Using readline()
data = open('data.txt', 'r')
count = 0

previousDepth = 10000000
increasedDepth = 0

l1 = int(data.readline().strip())
l2 = int(data.readline().strip())
l3 = int(data.readline().strip())

Acc1 = l1 + l2 + l3
Acc2 = l2 + l3
Acc3 = l3
previousAcc = 100000

while True:
 
    # Get next line from file
    line = data.readline()
 
    if not line:
        break
    currentDepth = int(line.strip())

    depthHasIncreased = Acc1 < Acc2 + currentDepth
    print("1:{}, 2:{}, 3:{}, c:{}, I:{}".format(Acc1, Acc2, Acc3, currentDepth, depthHasIncreased))
    if(depthHasIncreased):
        increasedDepth += 1
    
    Acc1 = Acc2 + currentDepth
    Acc2 = Acc3 + currentDepth
    Acc3 = currentDepth

print("# increasedDepth: {}".format(increasedDepth))
data.close()