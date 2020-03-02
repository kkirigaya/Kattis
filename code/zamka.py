l, d, x = map(int, [input(), input(), input()])

n, m = -1, -1

for _n in range(l, d+1):
    if sum(map(int, list(str(_n)))) == x:
        n = _n
        break

for _m in range(d, l-1, -1):
    if sum(map(int, list(str(_m)))) == x:
        m = _m
        break

print(n)
print(m)
