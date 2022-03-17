n = int(input())
aa = []
for i in range(1, n+1):
    if i % 2 == 0:
        if i != n:
            aa.append('I love that')
        else:
            aa.append('I love it')
    if i % 2 != 0:
        if i != n:
            aa.append('I hate that')
        else:
            aa.append('I hate it')
print(' '.join(aa))
