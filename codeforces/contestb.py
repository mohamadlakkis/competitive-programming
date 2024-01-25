t = int(input())
for i in range(t):
    n, k = list(map(int, input().split()))
    H = list(map(int, input().split()))
    P = list(map(int, input().split()))
    while k > 0:
        m = 99999
        for i in range(n):
            if H[i]-k >= 0:
                H[i] -= k
            else:
                H[i] = 0
            if m >= P[i] and H[i] != 0:
                m = P[i]

        k -= m
    c = 0
    for j in range(n):
        if H[j] != 0:
            print('NO')
            break
        if j == n-1:
            print('YES')
