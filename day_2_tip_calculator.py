# Welcome message
print("Welcome to the tip calculator!")

# Define variables
bill = float(input("How much was the total bill?"))
tip = int(input("What percentage tip would you like to leave?"))
people = int(input("How many people should split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = '{:.2f}'.format(bill_per_person)  # force two decimals

# Output
print(f"Each person should pay: R{final_amount}")