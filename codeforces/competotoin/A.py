t = int(input())
for i in range(0, t):
    n = int(input())
    L = [5, 7]
    for i in range(1, n - 1):
        L.append((L[i] + 2))
    for i in L:
        print(i, end=" ")
    print()
