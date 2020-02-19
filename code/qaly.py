n = int(input())

s = 0
for _ in range(n):
    q,y = map(float, input().split())
    s += q*y

print(str(s))
