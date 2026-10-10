# pass -> pass is used to neglect expected indentation error
for i in range(1,11):
    pass

# break -> break is used to terminate the flow of loop
for i in range(1,11):
    if(i==5):
        break
    print(i)
    # break directly do affect on loop once condition met loop will be terminated
# continue -> continue is used to skip current iteration
for i in range(1,11):
    if(i==5):
        continue
    print(i)
# continue doesn't affect on loop directly if only skips current iteration after that loop will execute

# else -> if loop execute successfully then else will execute
for i in range(1,11):
    if(i==5):
        break
    print(i)
else:
    print("Else execute")


for i in range(1,11):
    if(i==5):
        continue
    print(i)
else:
    print("Else execute")

