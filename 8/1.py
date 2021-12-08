import functools

data = open('8/data.txt', 'r')
signals = []
while True:
    line = data.readline()
    if not line:
        break
    signal = list(map(lambda x: x.strip().split(), line.strip().split('|')))
    signals.append((signal[0], signal[1]))

counter = 0
for signal in signals:
    for data in signal[1]:
        size = len(data)
        counter += 1 if size == 2 or size == 4 or size == 3 or size == 7 else 0

print(counter)

