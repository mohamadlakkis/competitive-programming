n = int(input())
s = input()
count_of_a = 0
count_of_d = 0
for i in range(0, len(s)):
    if s[i] == 'D':
        count_of_d += 1
    if s[i] == 'A':
        count_of_a += 1
if count_of_a > count_of_d:
    print('Anton')
if count_of_a < count_of_d:
    print('Danik')
if count_of_a == count_of_d:
    print('Friendship')
