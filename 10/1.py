import functools

def is_chunk_corrupted(chunk):
    openings = ['[','(','<','{']
    closings = [']',')','>','}']
    band = ""
    for char in chunk:
        if char in openings:
            band += char
        elif char in closings:
            lastChar = band[-1]
            if (lastChar == '(' and char == ')') or (lastChar == '[' and char == ']') or (lastChar == '{' and char == '}') or(lastChar == '<' and char == '>'):
                band = band[0:len(band)-1]
            else:
                return (True, char)
    return (False, '')



data = open('10/data.txt', 'r')
signals = []
while True:
    line = data.readline().strip()
    if not line:
        break
    signals.append(line)

char_score={')':3,']':57,'}':1197,'>':25137}
corruption_score = 0
for signal in signals:
    (corrupted, char) = is_chunk_corrupted(signal)
    if corrupted:
        corruption_score += char_score[char]
print(corruption_score)