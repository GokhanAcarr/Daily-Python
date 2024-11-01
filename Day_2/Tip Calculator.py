print("Welcome to Tip Calculator!")
totalBill = float(input("What was the total bill? $"))
tipPercentage = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
numberOfPeople = int(input("How many people to split the bill?"))
billPerPeople = (totalBill + (totalBill * tipPercentage / 100 )) / numberOfPeople
print(billPerPeople)
