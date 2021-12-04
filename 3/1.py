data = open('3/data.txt', 'r')
count = 0

report = []

# Load report file
while True:
    line = data.readline()
    if not line:
        break
    report.append(line.strip())

nbBits = len(report[0])
significantBitPerColumn = []

# Count significant bit per column
for bit in range(nbBits):
    significantBitPerColumn.append(0)
    for line in report:
        if line[bit] == '1':
            significantBitPerColumn[bit] += 1

print("significantBitPerColumn: {}".format(significantBitPerColumn))


gammaStr = ""

for val in significantBitPerColumn:
    if val > len(report)/2:
        gammaStr += '1'
    else:
        gammaStr += '0'

gamma = int(gammaStr,2)
print("gamma: {}".format(gamma))

epsilon = (pow(2, nbBits) - 1) - gamma

print("epsilon: {}".format(epsilon))
print("res: {}".format(epsilon * gamma))


data.close()