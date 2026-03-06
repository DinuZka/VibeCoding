# Ask for total monthly budget
budget = float(input("Enter total monthly budget: "))

total_expenses = 0

# Enter expenses repeatedly
while True:
    expense = input("Enter an expense (type 'done' to finish): ")
    
    if expense.lower() == "done":
        break
    
    total_expenses += float(expense)

# Calculate remaining balance
balance = budget - total_expenses

# Display balance
print("Total Expenses:", total_expenses)
print("Remaining Balance:", balance)

# Low funds warning
if balance < 500:
    print("Warning: Low Funds")