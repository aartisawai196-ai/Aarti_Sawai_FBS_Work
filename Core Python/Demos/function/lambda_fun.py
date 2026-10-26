# To reduce Lines of code
# one liner function
# always return 
# anonymous function
# function without name
# only single expression is there

# add=lambda n1,n2:n1+n2
# res=add(10,20)
# print(f"Addition is {res}")

# si=lambda p,r,t:(p*r*t/100)
# res=si(10000,7,2)

# print(f"simple interst is {res}")


# data=[1,2,3,4,5,6,7,8,9,10]

# def sq(n):
#     return n*n

# res=map(sq,data)
# print(list(res))

# method 2
data=[1,2,3,4,5,6,7,8,9,10]
res=list(filter(lambda n:n%2==0,data))
print(res)


