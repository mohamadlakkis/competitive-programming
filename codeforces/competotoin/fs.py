t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    if n <= 2:
        print('YES')
    else:
        if n % 2 == 0:
            s1 = s[0:n//2]
            s2 = s[n//2:n]
        else:
            s1 = s[0:n//2]
            s2 = s[n//2+1:n]
        j = len(s2)-1
        arr = []
        for i in range(len(s1)):
            if s1[i] != s2[j]:
                arr.append(False)
            else:
                arr.append(True)
            j -= 1
        c = True
        first_false = False
        for i in range(len(arr)-1):
            if arr[i] == False:
                first_false = True
            elif first_false == True and arr[i] == True and arr[i+1] == False:
                c = False
                break

        if c:
            print("YES")
        else:
            print('NO')
