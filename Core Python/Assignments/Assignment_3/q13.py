unit=int(input("Enter Units"))
if unit>50:
    rate1=50*0.50
    remaining_unit=unit-50

    if remaining_unit>=100:
        rate2=100*0.75
        remaining_units=remaining_unit-100

        if remaining_units>=100:
            rate3=100*1.20
            rem=remaining_units-100

            rate4=rem*1.50
        else:
             rate3=remaining_units*1.20
             rate4=0
    else:
        rate2=remaining_unit*0.75
        rate3=0
        rate4=0
else:
    rate1=unit*0.50
    rate2=0
    rate3=0
    rate4=0

bill=rate1+rate2+rate3+rate4
surcharge=bill*0.20
total=bill+surcharge

print(total)
