n, m = list(map(int, input().split()))
M = []
for i in range(n):
    mm = list(map(int, input().split()))
    M.append(mm)
zeroes = 0
Ones = []
for i in range(n):
    for j in range(m):
        if(M[i][j] == 0):
            zeroes += 1
        else:
            Ones.append([i, j])
i1 = 0
i2 = n-1
j1 = 0
j2 = m-1
kkkkk = False
for INDEX in Ones:
    if(i1 <= INDEX[0] <= i2 and j1 <= INDEX[1] <= j2):
        i = INDEX[0]
        j = INDEX[1]
        count = 0
        L = [[i-1, j-1], [i, j-1], [i+1, j-1], [i+1, j],
             [i-1, j], [i-1, j+1], [i, j+1], [i+1, j+1]]
        for w in L:
            if(0 <= w[0] <= n-1 and 0 <= w[1] <= m-1):
                if(M[w[0]][w[1]] == 0):
                    count += 1
        if count == zeroes:
            print("WIN")
            kkkkk = True
            break
if not kkkkk:
    print("LOSE")
    