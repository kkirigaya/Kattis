have = list(map(int, input().split()))
reqd = [1, 1, 2, 2, 2, 8]

s = ""
for i in range(len(have)):
    s += str(reqd[i] - have[i]) + " "

print(s)
