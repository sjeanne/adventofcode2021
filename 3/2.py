data = open('3/data.txt', 'r')
count = 0

def filterSignal(table, bitNumber, takeMostCommon):
    significantBitForColumn = 0

    # Count significant bit for the column
    for line in table:
        if line[bitNumber] == '1':
            significantBitForColumn += 1
    if(takeMostCommon):
        filterBitValue = '1' if (significantBitForColumn >= len(table) / 2) else '0'
    else:
        filterBitValue = '0' if (significantBitForColumn >= len(table) / 2) else '1'

    filteredTable = []
    for line in table:
        if line[bitNumber] == filterBitValue:
            filteredTable.append(line)

    print("Filter: bitNumber:{}, In:{}, Out:{}".format(bitNumber, len(table), len(filteredTable)))
    return filteredTable




report = []

while True:
    line = data.readline()
    if not line:
        break
    report.append(line.strip())

# Find oxygen
bitUsed = 0
oxygenValues = report
while len(oxygenValues) > 1:
    oxygenValues = filterSignal(oxygenValues,bitUsed, True)
    bitUsed += 1

print("Oxygen:{}".format(oxygenValues))

bitUsed = 0
co2 = report
while len(co2) > 1:
    co2 = filterSignal(co2,bitUsed, False)
    bitUsed += 1

print("co2:{}".format(co2))


print("result: {}".format(int(oxygenValues[0],2)* int(co2[0],2)))

data.close()