triangle = 21
for i in range(7, 100000000000000):
    triangle += i
    divisors = []
    for a in range(1, triangle+1):
        for b in range(1, triangle+1):
            if a*b == triangle and a not in divisors:
                divisors.append(a)
                divisors.append(b)
    if len(divisors) > 500:
        break
print(triangle)
