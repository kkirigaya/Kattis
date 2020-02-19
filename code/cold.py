n = int(input())
temps = map(int, input().split(" "))

print(len([t for t in temps if t < 0]))
