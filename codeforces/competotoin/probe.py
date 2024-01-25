t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    D = {'E':[],'O':[]}
    for i,m in enumerate(a):
        if m%2==0:
            D['E'].append(i)
        else:
            D['O'].append(i)
    if len(D['O'])>=3:
        print('YES')
        print(D['O'][0],D['O'][1],D['O'][2])
    else:
        if len(D['E'])>=2 and len(D['O'])>=1:
            print('YES')
            print(D['O'][0],D['E'][0],D['E'][1])
        else:
            print('NO')