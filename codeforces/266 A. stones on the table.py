nb_of_stones = int(input())
stones = input()
stones_last = stones + ' '+'a'
ct = 0
for i in range(0, len(stones)):
    if stones_last[i] == stones_last[i+1]:
        ct += 1
print(ct)
