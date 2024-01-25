t = int(input())
for i in range(t):
    a, b, c = list(map(int, input().split()))
    if a < b < c or a > b > c:
        print(b)
    elif b < a < c or c < a < b:
        print(a)
    elif a < c < b or b < c < a:
        print(c)
