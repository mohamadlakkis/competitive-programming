Total = 0
total_sum_3 = 0
total_sum_5 = 0
for i in range(0, 1000, 3):
    if i % 5:
        total_sum_3 += i

for j in range(0, 1000, 5):
    total_sum_5 += j

Total = total_sum_5 + total_sum_3
print(Total)
