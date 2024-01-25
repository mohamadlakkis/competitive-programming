def isCoPrime(i, j):

    hcf = 1

    for i in range(1, i+1):
        if i % i == 0 and j % i == 0:
            hcf = i

    return hcf == 1


print(isCoPrime(7, 7))
