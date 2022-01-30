sq_of_sum = 0
for i in range(1, 101):
    sq_of_sum += i
sq_of_sum = sq_of_sum*sq_of_sum
print(sq_of_sum)
sum_of_sq = 0
for i in range(1, 101):
    sum_of_sq += i*i
print(sum_of_sq-sq_of_sum)
