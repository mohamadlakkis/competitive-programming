n = int(input())
last = 0
for i in range(1, n+1):
    if i % 2 == 0:
        last += i
    else:
        last += (-i)
print(last)
