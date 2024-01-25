arr = list(map(int, input().split()))

# Change positive numbers to 1 and negative numbers to -1
arr = [1 if x > 0 else -1 for x in arr]

# Sort the array
arr.sort()

# Calculate max_list
cumulative_sum = 0
max_list = []
for num in arr:
    if cumulative_sum + num > 0:
        cumulative_sum += num
        max_list.append(cumulative_sum)
    else:
        max_list.append(0)

# Calculate min_list
min_list = []
i = 0
j = len(arr) - 1
while i <= j:
    if i == j:
        min_list.append(arr[i])
    else:
        min_list.append(arr[i])
        min_list.append(arr[j])
    i += 1
    j -= 1
    if i == j:
        min_list.append(arr[i])
print(max_list)
print(min_list)
