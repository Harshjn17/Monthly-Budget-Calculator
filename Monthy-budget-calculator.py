user = input("Enter your Name: ") 
print(f"Welcome! {user} ji")
income = float(input("Enter your Monthly income: "))

#Expenses
Food = float(input("Enter your Food cost: "))
groceries = float(input("Enter your groceries cost: "))
Transportation = float(input("Enter your Transportation cost: "))
Entertainment = float(input("Enter your Entertainment cost: "))
Utilities = float(input("Enter your Utilities cost: "))
Other_expenses = float(input("Enter your Other expenses cost: "))

#Add Expenses
expenses_total = Food + groceries + Transportation + Entertainment + Utilities + Other_expenses

# Income left
remaining_income = income - expenses_total

#compare
if income > expenses_total:
    print(f"Great! You saved ₹{remaining_income} this month!")
elif remaining_income == 0:
    print(f"You broke even")
elif income < expenses_total:
    print(f"Warning! You overspent by ₹{abs(remaining_income)}")
    
# Calculate spending

spending = (expenses_total / income) * 100

# check category
max_category = max(Food,Other_expenses,Utilities,Entertainment,Transportation,groceries)
result = ""
if Food == max_category:
    result = "Food"
elif groceries == max_category:
    result = "groceries"
elif Transportation == max_category:
    result = "Transportation"
elif Other_expenses == max_category:
    result = "Other_expenses"
elif Entertainment == max_category:
    result = "Entertainment"
elif Utilities == max_category:
    result = "Utilities"

 
# budget summary
print("\n========== BUDGET SUMMARY ==========")
print(f"Total Income:      ₹{income}")
print(f"Total Expenses:    ₹{expenses_total}")
print(f"Remaining Budget:  ₹{remaining_income}")
print(f"Spending:          {spending:.2f}%")
print(f"Top Category:      {result}")
print("====================================")
