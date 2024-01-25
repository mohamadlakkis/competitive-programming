t = int(input())
for k in range(t):
    n = int(input())
    a = list(int(num) for num in input().strip().split())[:n]
    nbofvalleys_total = 0
    l = 0
    while l <= n-1:
        r = l
        nbofvalleys = 0
        while r <= n-1 and a[l] == a[r]:
            if l == 0 or a[l-1] > a[l]:
                if r == n-1 or a[r] < a[r+1]:
                    nbofvalleys += 1
                    l = r
            r += 1
        if nbofvalleys != 0:
            nbofvalleys_total += 1
        l += 1
    if nbofvalleys_total == 0:
        print('NO')
    elif nbofvalleys_total == 1:
        print('YES')
    else:
        print('NO')
