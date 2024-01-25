t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if a == 3:
        print(-1)
    else:
        i = 0
        j = len(a)-1
        m = max(a)
        u = min(a)
        if m == a[j] and a[i] == u:
            print(i, j)
        elif m == a[i] and u == a[j]:
            print(i, j)
        else:

            i = 0
            j = 3
            c_max = max(a[i], a[i+1], a[j-1], a[j])
            c_min = min(a[i], a[i+1], a[j-1], a[j])
            if c_max != a[j] and c_min != a[i] and c_max != a[i] and c_min != a[j]:
                print(i, j)
