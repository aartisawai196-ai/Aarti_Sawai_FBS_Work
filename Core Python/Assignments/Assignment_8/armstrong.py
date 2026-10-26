
def count_digit(n):
    return len(str(n))

def calculate_armstrong(n):
    temp=n
    power=count_digit(n)
    total=0
    while temp>0:
        digit=temp%10
        total=total+digit**power
        temp=temp//10
    return total

def check_armstrong(n):
    if calculate_armstrong(n)==n:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")

n=int(input("Enter number..."))
check_armstrong(n)