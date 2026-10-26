#Accept no of passengers  from user and per ticket cost then accept the age of 
# each  passenger and then calculate the total amount to ticket to travel for all of them based on following condition
# a. children below 12 = 30% discount
# b. senior citizen(above 59) = 50% discount
# others need to pay full

no_of_passengers=int(input("Enter number of passengers"))
total_amt=0
for i in range(1,no_of_passengers+1):
    cost=int(input(f"Enter ticket cost of {i} passenger "))
    age=int(input(f"Enter age of {i} person"))

    total_amt=cost

    if(age<12):
        dis=total_amt*30/100
        print(total_amt-dis)
    elif(age>59):
        discount=(total_amt*50)/100
        print(total_amt-discount)
    else:
        print("you need to pay full bill...")