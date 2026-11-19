s=int(input("Enter number"))
idx=0
li=[1,2,3,4,5,6]
found=False
for i in range(0,len(li)):
    if s==li[i]:
        found=True
    
    else:
        found=False
if found==True:
    print("found at index {idx}")
else:
    print("not found")