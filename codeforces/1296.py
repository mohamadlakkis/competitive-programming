t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    su = 0
    for i in a:
        su += i
    if su % 2 != 0:
        print('YEs')
    else:

        even = 0
        odd = 0
        for i in a:
            if i % 2 == 0:
                even += 1
            if i % 2 != 0:
                odd += 1
            if even != 0 and odd != 0:
                break
        if even != 0 and odd != 0:
            print('YES')
        else:
            print('NO')
