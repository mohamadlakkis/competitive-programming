t = int(input())
for i in range(t):
    n = int(input())
    health = list(map(int, input().split()))
    health.sort()
    health.reverse()
    count = 0
    for i in range(len(health)-1):
        if health[i]==1:
            count+=1
            health[i]=0
            health[i+1] -=1
        elif health[i]!=0:
            health[i]=0 
            count +=1
    if health[n-1]!=0:
        count +=1
    print(count)



            

