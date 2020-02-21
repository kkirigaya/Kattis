t = int(input())

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

for _ in range(t):
    n = int(input())
    print(str(factorial(n))[-1])
