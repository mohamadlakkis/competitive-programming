k, n, w = list(map(int, input().split()))
cost_of_all_bananas = 0
for i in range(1, w+1):

    cost_of_all_bananas += i*k
money_from_friend = cost_of_all_bananas-n
if money_from_friend > 0:
    print(money_from_friend)
else:
    print(0)
