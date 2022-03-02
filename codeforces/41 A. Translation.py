s = input()
inverse = input()
letters = []
for i in range(len(inverse)-1, -1, -1):
    letters.append(inverse[i])
final = ''.join(letters)
if final.lower() == s.lower():
    print('YES')
else:
    print('NO')
