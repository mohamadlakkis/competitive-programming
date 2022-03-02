n = int(input())
first = []
second = []
j = 0
while j < n:
    a, b = list(map(int, input().split()))
    first.append(a)
    second.append(b)
    j += 1
highest_number = 0
remaining = 0
for i in range(0, n):
    remaining = remaining - first[i]
    remaining = remaining + second[i]
    if remaining > highest_number:
        highest_number = remaining
print(highest_number)
