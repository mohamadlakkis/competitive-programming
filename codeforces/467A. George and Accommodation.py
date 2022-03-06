capacity = []
already = []
n = int(input())
for i in range(0, n):
    a, b = list(map(int, input().split()))
    already.append(a)
    capacity.append(b)
nb = 0
for i in range(0, n):
    if capacity[i] - already[i] >= 2:
        nb += 1
print(nb)
