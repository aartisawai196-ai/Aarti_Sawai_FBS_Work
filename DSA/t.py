t1=(1,2,1,1,3)
t2=(1,2,3,5)
print(id(t1),id(t2))
print(t1.count(1))
print(t1.index(3))
print(sorted(t1))
print(max(t1))
print(min(t1))
print(sum(t1))
#

t3=("ram","shyam","sita")
for i,j in enumerate(t3):
    print(i,j)