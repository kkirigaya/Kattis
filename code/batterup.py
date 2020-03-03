input() # don't need first line

n = list(map(int, input().split()))
n = list(filter(lambda x: not x == -1, n)) # remove walks (value == -1)
print(sum(n)/len(n))
