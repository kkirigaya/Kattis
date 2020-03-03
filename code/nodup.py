l = input()

words = []
for word in l.split():
    if word in words:
        print("no")
        break
    words.append(word)
else:
    print("yes")
