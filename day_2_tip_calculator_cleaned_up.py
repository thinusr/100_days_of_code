# Welcome message
print("Welcome to the tip calculator!")

# Get user input and calculate final amount per person
bill = float(input("Enter the total bill amount: \n"))
tip = float(input("Enter the tip percentage: \n"))
people = int(input("Enter the number of people splitting the bill: \n"))

# Calculate total and per-person amounts
final_amount = (bill * (1 + tip / 100)) / people

# Output
print(f"Each person should pay: R{final_amount:.2f}")

# Here's a cleaned-up and simplified version of the code.
# It retains functionality while improving readability and structure:
#
# Improvements:
# Removed unnecessary variables:
# Calculations for tip_as_percent, total_tip_amount, and total_bill are now done inline.
# Simplified input prompts:
# Clearer and more concise messages for user inputs.
# Direct formatting:
# :.2f is applied directly in the output statement for better readability and fewer intermediate steps.
