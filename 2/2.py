# Using readline()
data = open('2/data.txt', 'r')
count = 0

X = 0
Y = 0
Aim = 0

while True:
    line = data.readline()
 
    if not line:
        break

    command, value = line.split(' ')
    if(command == "forward"):
        X += int(value)
        Y += int(value) * Aim
    elif command =="down":
        Aim += int(value)
    elif command =="up":
        Aim -= int(value)

    print("X:{}, Y:{}, C:{}, V:{}".format(X,Y,command, value))
    

print("# X*Y: {}".format(X*Y))
data.close()