#This is the bill disttributer. 
your_bill = float(input("How much is your bill. $"))
tip = float(input("how much tip you want to give ,10,11,12,etc. %"))
split = float(input("How many people to split the bill No."))
tip_in_persentag = (tip / 100)
tip_multipay = (tip_in_persentag*your_bill)
tip_wiht_bill = (tip_multipay + your_bill)
split_bill = (tip_wiht_bill/ split )
print (round(split_bill,2))  