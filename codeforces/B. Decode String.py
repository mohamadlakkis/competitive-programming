q = int(input())
for x in range(q):
    n = int(input())
    t = input()  # contains the code in a string format
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    l = []
    m = n-1
    while m >= 0:
        if t[m] != '0':
            l.append(alphabet[m])
            m -= 1
        else:
            twoletters = t[m-2:m]
            l.append(alphabet[int(twoletters)-1])
            m -= 3
    rev = l.reverse()
    print(''.join(map(str, rev)))
