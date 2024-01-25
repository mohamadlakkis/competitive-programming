t = int(input())
all_list = []

for i in range(0, t):
    a, b = list(map(int, input().split()))
    all_list.append([a, b])

for m in range(t):
    nb_of_moves = 0
    if all_list[m][0] < all_list[m][1] or (all_list[m][0] % all_list[m][1]) != 0:

        while all_list[m][0] < all_list[m][1] or (all_list[m][0] % all_list[m][1]) != 0:
            nb_of_moves += 1
            all_list[m][0] += 1
        print(nb_of_moves)

    else:
        print(0)
