print("Tip Calculator!")
bill= float(input("What was the total bill? $"))
tip= int(input("What percentage tip would you like to give? 10 12 15"))
people = int(input("How many people you want to split the bill?"))
tip_percent= tip/100
totaltip = bill * tip_percent
totalbill = bill + totaltip
bill_person = totalbill / people 
final_amount = round(bill_person , 2)
print(f"Each person shouls pay : ${final_amount} ")