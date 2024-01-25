t  = int(input())
for i in range(t):
    number_of_types = int(input())
    number_of_candies_of_each_type = list(map(int, input().split()))
    
    if (number_of_types == 1 and number_of_candies_of_each_type[0]!=1):
        print('NO')
    else:
        number_of_candies_of_each_type.sort(reverse=True)
        
        
        if number_of_types == 1 and number_of_candies_of_each_type[0]==1:
            print('YEs')
        elif number_of_candies_of_each_type[0]== number_of_candies_of_each_type[1]:
            print('YES')
        elif number_of_candies_of_each_type[0]== number_of_candies_of_each_type[1]+1:
            print('YES')
        else:
            print('NO')
