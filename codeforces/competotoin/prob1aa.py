t = int(input())
for i in range(t):
    n = int(input())
    health = list(map(int, input().split()))
    health.sort()
    count = 0
    i = 0
    j = n-1
    while i<=j:
        if health[i]==0:
            i+=1
            if health[j]!=0:
                    health[j]=0
                    j-=1
                    count+=1
        else:
            if health[i+1]!=0:
                health[i]-=1
                health[i+1]-=1
                count +=1
                if health[j]!=0:
                    health[j]=0
                    j-=1
                    count+=1
            else:
                i+=2
            
    print(count)
        