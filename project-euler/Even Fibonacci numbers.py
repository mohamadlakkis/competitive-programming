from tkinter import N


a = 1
b = 2
c = 3
n = 2
while n <= 4000000:
    a = b + c
    b = a+c
    c = a + b
    n += b
print(n)
