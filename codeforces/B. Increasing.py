t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = sorted(a)
    k = []
    c = 0
    for i in range(n):
        if m[i] not in k:
            c += 1
            k.append(m[i])
    if len(k) == n:
        print('yes')
    else:
        print('no')
