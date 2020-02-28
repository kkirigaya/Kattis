n = int(input())

for _ in range(n):
    a, b, s = input(), input(), ""

    for i in range(len(a)):
        ca, cb = a[i], b[i]
        if ca == cb:
            s += '.'
        else:
            s += '*'

    print(a)
    print(b)
    print(s)
