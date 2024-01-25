t = int(input())
nb_0 = 0
nb_pos = 0
nb_neg = 0
avg_pos = 0
avg_neg = 0
neg = False
pos = False

for i in range(t):
    current = int(input())
    if current ==0:
        nb_0 +=1
    elif current>0:
        pos = True
        
        avg_pos = avg_pos*nb_pos
        nb_pos +=1
        avg_pos = (avg_pos+current)/nb_pos

    else:
        neg = True
        avg_neg = avg_neg*nb_neg
        nb_neg +=1
        avg_neg = (avg_neg+current)/nb_neg

    print('nb of zeroes= ',nb_0)
    if neg ==False:
        print('No negative numbers')
    else:
        print('average of negative numbers = ',avg_neg)
    if pos ==False:
        print('No postive numbers')
    else:
        print('average of postive numbers = ',avg_pos)
