def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


count = 2
i = 3
while count < 10001:
    i += 2
    if is_prime(i):
        count += 1
print(i)
