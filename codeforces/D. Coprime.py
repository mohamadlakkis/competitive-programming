def isCoPrime(i, j):

    hcf = 1

    for i in range(1, i+1):
        if i % i == 0 and j % i == 0:
            hcf = i

    return hcf == 1


t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    su = -1
    for i in range(n):
        for j in range(i, n):
            if isCoPrime(a[i], a[j]) and (i+j) >= su:
                su = i+j
    print(su)
