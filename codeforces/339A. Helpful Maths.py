count_nb_1 = 0
count_nb_2 = 0
count_nb_3 = 0
inputttt = input()
for i in range(0, len(inputttt)):
    if inputttt[i] == '1':
        count_nb_1 += 1
    if inputttt[i] == '2':
        count_nb_2 += 1
    if inputttt[i] == '3':
        count_nb_3 += 1
x = '1+'*count_nb_1 + '2+'*count_nb_2 + '3+'*count_nb_3
x = x[:-1]
print(x)
