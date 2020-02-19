n,w,h = map(int, input().split())

ms = []
for _ in range(n):
    ms.append(int(input()))

for m in ms:
    print("DA" if m <= (w**2 + h**2)**.5 else "NE")
