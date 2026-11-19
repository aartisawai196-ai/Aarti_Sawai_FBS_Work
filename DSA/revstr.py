s1="aarti"
rev=""
for i in range(len(s1)-1,-1,-1):
    rev+=s1[i]
print(rev)


rev=""             
for ch in s1:
    rev=ch+rev
print(rev)

# slicing
print(s1[::-1])
