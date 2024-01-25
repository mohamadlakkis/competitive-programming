x, y, z, m = list(map(int, input().split()))
lisst_ = [x, y, z, m]
largest = max(lisst_)
for i in lisst_:
    if largest - i != 0:
        print(largest-i)
