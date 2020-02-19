x = int(input())
n = int(input())

pool = x
for _ in range(n):
    pool += x - int(input())

print(pool)
