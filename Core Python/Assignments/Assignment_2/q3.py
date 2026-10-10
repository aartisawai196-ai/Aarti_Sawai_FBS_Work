# write a program to convert given distance into centimeters and meters

feet=int(input("Enter Distance in Feet :"))
inches=int(input("Enter Distance in inches :"))

inch=feet*12
total_inches=inch+inches
total_centimeter=total_inches*2.54
remaining_centimeter=total_centimeter%100
meter=total_centimeter/100

print(total_inches,inch,remaining_centimeter)
print("Centimeter is :",total_centimeter)
print("Meter is :",meter)