n = int(input())
opinions = list(map(int, input().split()))
c = 0
for i in range(0, n):
    if opinions[i] == 0:
        c += 1
    if opinions[i] == 1:
        print('HARD')
        break
if c == len(opinions):
    print('EASY')
