print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? "))

percentage = int(input("What percentage tip would you like to give? 10,12 or 15? "))

split = int(input("How many people to split the bill? "))

pay = ((bill * (percentage/100)) + bill) /split
pay = (round(pay,2))
pay = "{:.2f}".format(pay)
print(f"Each person should pay: {pay}")