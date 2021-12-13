import functools

data = open('xx/data.txt', 'r')

while True:
    line = data.readline().strip()
    if not line:
        break
    pass