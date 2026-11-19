rev=0
def reverse(n):
        d=n%10
        rev=d
        n=n//10
        return reverse(n>0)
    
n=int(input("Enter number :"))
rs=reverse(n)
print(f"reverse is {rs}")
