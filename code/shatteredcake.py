w, n = map(int, [input(), input()])

total = 0
for _ in range(n):
    wi, li = map(int, input().split())

    v = wi*li
    total += v

print(total//w)
