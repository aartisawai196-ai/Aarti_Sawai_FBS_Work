#why because it is dificult to store large numbers within some range in a single variable
#what range function is used to generate sequence of numbers

#how->syntax
# range(start,stop,step)
# start is an inclusive parameter wwhich is use for starting ,by default it is 0 
# stop  is an exclusive parameter ehich is use for ending
# step is use for increament and by default step is +1

for i in range(1,11):
    print(i)

for i in range(10,1,-1):
    print(i)

n=int(input("entr number"))
for i in range(n,n*10+1,n):
    print(i)

    