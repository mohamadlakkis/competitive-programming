t = int(input())
for i in range(t):
    n = int(input())
    a = list(int(num) for num in input().strip().split())[:n]
    result = []
    m = a[0]
    p = 0
    for j in range(1, len(a)):
        if a[j] > m:
            m = a[j]
            p = j
    if m != a[0]:
        n = a[0]
    else:
        n = a[1]
    for k in range(0, len(a)):
        if k != p:
            if n < a[k]:
                n = a[k]
    for q in range(0, len(a)):
        if a[q] != m:
            result.append(a[q]-m)
        else:
            result.append(a[q]-n)
    print(*result)
