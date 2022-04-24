fr = input()
sec = input()
num = []
for i in range(0, len(fr)):
    if fr[i] == sec[i]:
        num.append('0')
    else:
        num.append('1')
num = ''.join(num)
print(num)
