import math

a, i = map(int, input().split())

x = 0
while True:
    b = x/a

    if math.ceil(b/a) == i:
        print(math.ceil(b))
        break
    else:
        x += 1
