t = int(input())
for i in range(t):
    n = int(input())  # number of days Dasha has a plan for
    plan = list(map(int, input().split()))  # Dasha's plan

    male = 0  # number of male guinea pigs
    female = 0  # number of female guinea pigs
    aviaries = 0  # number of aviaries needed

    for j in range(n):
        if plan[j] == 1:  # Dasha buys a new guinea pig
            if male <= female:  # if there are more or equal number of males than females
                male += 1
                aviaries += 1  # a new aviary is needed
            else:  # if there are more females than males
                female += 1
                aviaries += 1  # a new aviary is needed
        else:  # the doctor examines the guinea pigs
            if male < female:  # if there are more females than males
                male, female = female, male  # swap the number of males and females
            aviaries += male  # the number of aviaries needed is equal to the number of male guinea pigs
            female = 0  # reset the number of female guinea pigs
    print(aviaries)
