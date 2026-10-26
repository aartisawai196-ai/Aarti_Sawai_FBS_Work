#write a program to check if entered number is palindrome or not

def palindrome(n):
    rev=0
    temp=n
    while n>0:
        d=n%10
        rev=rev*10+d
        n=n//10
    if(rev==temp):
        print(f"{temp} is palindrome !")
    else:
        print(f"{temp} is not palindrome !")


n=int(input("Enter numebr:"))
palindrome(n)