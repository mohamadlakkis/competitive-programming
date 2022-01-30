n = int(input())
count = 0
for i in range(n):
    m = input()
    if m == '++X' or m == 'X++':
        count += 1
    else:
        count = count - 1
print(count)
