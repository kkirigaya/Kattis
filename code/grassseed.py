c = float(input())
l = int(input())

s = 0
for _ in range(l):
    wi, li = map(float, input().split())

    s += wi * li

print(c * s)
