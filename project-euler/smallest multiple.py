

for number in range(2520, 10000000000, 20):
    a = 0
    for i in range(1, 21):
        if number % i == 0:
            a += 1
    if a == 20:
        print(number)
        break
