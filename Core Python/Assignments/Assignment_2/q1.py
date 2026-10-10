# write a program to convert time into secondas input hh,min,__spec__

hh=int(input("Enter time in hours :"))
min=int(input("Enter time in minutes"))
sec=int(input("Enter time in seconds :"))

total_seconds=(hh*3600+min*60+sec)

print("Time in seconds will be :",total_seconds,"sec")