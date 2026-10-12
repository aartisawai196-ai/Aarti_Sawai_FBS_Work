# write a program to draw following pattern
# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1

for i in range(1,6):
    for j in range(1,i+1):
        print(6-j,end=" ")
    print()