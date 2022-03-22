m = list(map(int, input().split()))
x = 0
nuber = set(m)
for i in nuber:
    x += m.count(i) - 1
print(x)
