blimps = []

for _ in range(5):
    blimps.append(input())

s = []
for i in range(len(blimps)):
    if "FBI" in blimps[i]:
        s.append(str(i+1))

if s:
    print(" ".join(s))
else:
    print("HE GOT AWAY!")
