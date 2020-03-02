while True:
    n = int(input())
    if n == -1:
        break

    last_elapsed = 0
    distance = 0
    
    for _ in range(n):
        s, t = map(int, input().split())
        _t = t - last_elapsed
        distance += s * _t
        last_elapsed = t

    print(distance, "miles")
