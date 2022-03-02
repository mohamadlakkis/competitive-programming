n = int(input())
number = [int(x) for x in str(n)]
count_of_lucky = 0
for i in range(0, len(number)):
    if number[i] == 4 or number[i] == 7:
        count_of_lucky += 1
lucky_number = [int(x) for x in str(count_of_lucky)]
aa = 0
for i in range(0, len(lucky_number)):
    if lucky_number[i] == 4 or lucky_number[i] == 7:
        aa += 1
if aa == len(lucky_number):
    print('YES')
else:
    print('NO')
