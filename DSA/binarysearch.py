li=[3,7,9,11,12,45,56,8,90]
def binarySearch(li):
    li.sort()
    tar=int(input("Enter no :!!!"))
    start=0
    end=len(li)-1
    while(start<=end):
        mid=(start+end)//2
        if tar==li[mid]:
            return mid
        elif tar>li[mid]:
            start=mid+1
        else:
            end=mid-1
    else:
        return -1

res=binarySearch(li)
if res==-1:
    print("not fpound")
else:
    print(f"found at index {res} ")