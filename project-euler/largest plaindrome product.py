for i in range(100, 1000):
    for j in range(100, 1000):
        number_1 = i*j
        if len(str(number_1)) == 6 and str(number_1)[0] == str(number_1)[5] and str(number_1)[1] == str(number_1)[4] and str(number_1)[2] == str(number_1)[3] and str(number_1)[0] == '8':
            print(number_1)
        j += 1
    i += 1
