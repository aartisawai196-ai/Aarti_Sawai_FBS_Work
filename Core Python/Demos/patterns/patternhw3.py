# write a program to draw following pattern
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

for i in range(1,6):
   for j in range(1,7-i):
        print(7-i-j,end=" ")
   print() 
