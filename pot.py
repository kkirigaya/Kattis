n = int(input())

s = 0
for _ in range(n):
    inp = input()
    p = int(inp[:-1])
    i = int(inp[-1])
    s += p**i

print(s)
