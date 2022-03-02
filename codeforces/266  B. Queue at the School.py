n, t = list(map(int, input().split()))
s = input()
j = 0
s = list(s)
while j < t:
    f = 0
    while f < n-1:
        if s[f] == 'B' and s[f+1] == 'G':
            s[f] = 'G'
            s[f+1] = 'B'
            f += 2
        else:
            f += 1
    j += 1
m = ''.join(s)
print(m)
