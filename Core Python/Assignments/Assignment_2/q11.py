# write a program to accept an integer amount from user and tell minimum number of notes needed for reperesenting that amount 
amt=int(input("Enter amount"))

note_2000=amt//2000
rem_amt=amt%2000
note_500=rem_amt//500
rem=rem_amt%500
note_100=rem//100
r=rem%100

print("2000 note :",note_2000)
print("500 note :",note_500)
print("100 note :",note_100)