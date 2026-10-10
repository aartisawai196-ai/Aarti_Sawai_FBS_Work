# is
x=10
y=10
l1=[10,20]
l2=[10,20]

print(x is y)
print("x :=",id(x),"y :=",id(y))

print(l1 is l2)
print("l1 :=",id(l1), "l2 :=",id(l2))
print("x :=",id(x),"y :=",id(y))
print(id(l1[0]),id(l2[0]))
# is not 

print(x is not y)