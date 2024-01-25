t = int(input())
for i in range(t):
    a, b, c = list(map(int, input().split()))
    if a != 1:

        if abs(a-1) < (abs(b-c)+abs(c-1)):
            print(1)
        elif abs(a-1) > (abs(b-c)+abs(c-1)):
            print(2)
        else:
            print(3)
    else:
        print(1)
