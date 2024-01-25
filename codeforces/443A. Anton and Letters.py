l = input()
letters = []
if len(l) != 2:
    for i in range(len(l)):
        if l[i] == ',' and l[i-1] not in letters:
            letters.append(l[i-1])
        elif i == len(l)-1 and l[i-1] not in letters:
            letters.append(l[i-1])
    print(len(letters))
else:
    print(0)
