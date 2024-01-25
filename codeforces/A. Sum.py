t = int(input())
for i in range(t):
    a, b, c = list(map(int, input().split()))
    if a == (b+c):
        print('yes')
    elif (a+b) == c:
        print('yes')
    elif (a+c) == b:
        print('yes')
    else:
        print('no')
