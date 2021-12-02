# Using readline()
data = open('2/data.txt', 'r')
count = 0

X = 0
Y = 0

while True:
    line = data.readline()
 
    if not line:
        break

    command, value = line.split(' ')
    if(command == "forward"):
        X += int(value)
    elif command =="down":
        Y += int(value)
    elif command =="up":
        Y -= int(value)

    print("X:{}, Y:{}, C:{}, V:{}".format(X,Y,command, value))
    

print("# X*Y: {}".format(X*Y))
data.close()