#write a program to create three lists of numbers, thier squares and cubes

num=[1,2,3,4,9,5,7]
square=[]
cube=[]

for i in range(len(num)):
    square.append(num[i]**2)
    cube.append(num[i]**3)

print(f'list :={num}')
print(f'square of list :={square}')
print(f'cube of list :={cube}')