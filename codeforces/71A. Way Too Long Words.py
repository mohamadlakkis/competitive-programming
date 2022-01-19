n = int(input())
list_all = []
for i in range(0, n):
    name = input()
    list_all.append(name)
for j in range(0, n):
    if len(list_all[j]) > 10:
        print(f"{list_all[j][0]}{len(list_all[j])-2}{list_all[j][-1]}")
    else:
        print(list_all[j])
