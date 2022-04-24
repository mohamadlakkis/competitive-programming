n = int(input())
pour = list(map(int, input().split()))
total = 0
for i in range(0, n):
    total += pour[i]
result = total/n
print(result)
