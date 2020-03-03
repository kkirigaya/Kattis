cups = [True, False, False]
steps = list(input())

for c in list(steps):
    if c == 'A':
        _ = cups[0]
        cups[0] = cups[1]
        cups[1] = _
    elif c == 'B':
        _ = cups[1]
        cups[1] = cups[2]
        cups[2] = _
    else:
        _ = cups[0]
        cups[0] = cups[2]
        cups[2] = _

print(cups.index(True)+1)
