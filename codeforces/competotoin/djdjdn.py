x = input("Enter string:")
n = len(x)
isPalindrome = True


for i in range(n):
    if x[i] != x[n - 1 - i]:
        isPalindrome = False
        break

    else:
        isPalindrome = True
if isPalindrome == True:
    print("YES palindrome")
else:
    print("NOT a palindrome")
