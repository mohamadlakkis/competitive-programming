list_1 = []
for number in range(2, 1000000):
    j = number
    terms = 0
    while j != 1:
        if j % 2 == 0:
            j = j/2
            terms += 1
        else:
            j = (3*j) + 1
            terms += 1
    if j == 1:
        terms += 1
    if terms == 525:
        print(number)
    # list_1.append(terms)
# print(list_1)
##last = 0
# for j in range(0, len(list_1)):
 #   if last < list_1[j]:
  #      last = list_1[j]
# print(last)
