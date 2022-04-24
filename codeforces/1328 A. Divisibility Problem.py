t = int(input())
list_of_a = []
list_of_b = []
for i in range(0, t):
    a, b = list(map(int, input().split()))
    list_of_a.append(a)
    list_of_b.append(b)
final_list = []
for i in range(0, t):
    if list_of_a[i] % list_of_b[i] != 0:
        coutnnt = 0
        while list_of_a[i] % list_of_b[i] != 0:
            list_of_a[i] += 1
            coutnnt += 1
        final_list.append(coutnnt)
    else:
        final_list.append(0)

for i in range(0, t):
    print(final_list[i])
