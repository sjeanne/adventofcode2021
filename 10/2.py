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
                return (True,'')
    return (False, band)

def end_incomplete_chunk(chunk):
    bracket_match= {'(':')','<':'>','[':']','{':'}'}
    (corrupted, band) = is_chunk_corrupted(chunk)
    if corrupted:
        return ""
    complete = ""
    for char in band[::-1]:
        complete += bracket_match[char]
    return complete
    



data = open('10/data.txt', 'r')
signals = []
while True:
    line = data.readline().strip()
    if not line:
        break
    signals.append(line)

char_score={')':1,']':2,'}':3,'>':4}
corruption_scores  = []
for signal in signals:
    comp = end_incomplete_chunk(signal)
    if comp:
        score = 0
        for c in comp:
            score *= 5
            score += char_score[c]
        print(comp, score)
        corruption_scores.append(score)
corruption_scores.sort()
print(corruption_scores[(len(corruption_scores)//2)])
