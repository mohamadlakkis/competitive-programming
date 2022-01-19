n = int(input())
list_all = []
for i in range(0, n):
    k = (input())  # 1 0 1
    list_all.append(k)
nb_of_problems = 0
for j in range(0, n):
    count = 0
    if list_all[j][0] == '1':
        count += 1

    if list_all[j][2] == '1':
        count += 1

    if list_all[j][4] == '1':
        count += 1

    if count > 1:
        nb_of_problems += 1
print(nb_of_problems)
