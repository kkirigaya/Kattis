n, h, v = map(int, input().split(' '))

p1 = (v - 0) * (h - 0) * 4
p2 = (n - v) * (h - 0) * 4
p3 = (v - 0) * (n - h) * 4
p4 = (n - v) * (n - h) * 4

print(max(p1,p2,p3,p4))
