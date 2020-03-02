a = map(int, input().split())
b = map(int, input().split())
c = map(int, input().split())
d = map(int, input().split())
e = map(int, input().split())
_a, _b, _c, _d, _e = sum(a), sum(b), sum(c), sum(d), sum(e)

m = max(_a, _b, _c, _d, _e)

if m == _a:
    print(1, _a)
elif m == _b:
    print(2, _b)
elif m == _c:
    print(3, _c)
elif m == _d:
    print(4, _d)
elif m == _e:
    print(5, _e)
