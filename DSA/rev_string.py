# li=[1,2,3,4,5,6]
# rev_list=[]
# for i in range(len(li)-1,-1,-1):
#     rev_list.append(li[i])
# print(f"reverse list {rev_list}")

li=[1,2,3,4,5,6]

left=0
right=len(li)-1

print(f"Before reversing {li}")
while left<=right:
    li[left],li[right]=li[right],li[left]
    left+=1
    right-=1
print(f"After reversing :{li}")