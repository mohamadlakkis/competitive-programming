t = int(input())
for i in range(t):
    a, b = input().split()
    if a[-1] == b[-1] == 'S':
        counta = 0
        for i in range(0, len(a)):
            if a[i] == 'X':
                counta += 1
        countb = 0
        for i in range(0, len(b)):
            if b[i] == 'X':
                countb += 1
        if counta == countb:
            print('=')
        elif counta > countb:
            print('<')
        elif counta < countb:
            print('>')
        else:
            print('=')
    elif a[-1] == b[-1] == 'L':
        counta = 0
        for i in range(0, len(a)):
            if a[i] == 'X':
                counta += 1
        countb = 0
        for i in range(0, len(b)):
            if b[i] == 'X':
                countb += 1
        if counta == countb:
            print('=')
        elif counta > countb:
            print('>')
        elif counta < countb:
            print('<')
        else:
            print('=')
    elif a[-1] == b[-1] == 'M':
        print('=')
    else:
        if a[-1] == 'L':
            print('>')
        elif a[-1] == 'S':
            print('<')
        elif a[-1] == 'M' and b[-1] == 'L':
            print('<')
        else:
            print('>')
