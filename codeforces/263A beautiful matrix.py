i, j = None, None
for i in range(1, 6):
    row = input()
    if '1' in row:
        j = (row.find('1') // 2) + 1
        break
min_moves = abs(3 - i) + abs(3 - j)  # Manhattan distance
print(min_moves)
