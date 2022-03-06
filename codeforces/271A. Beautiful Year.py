y = int(input())
for i in range(y, 100000):
    i += 1
    l = str(i)
    ra = []
    for j in range(0, len(l)):
        if l[j] not in ra:
            ra.append(l[j])
    if len(ra) == len(l):
        break


def integersss(ra): return int(''.join(str(i) for i in ra))  # Generator exp.


print(integersss(ra))
