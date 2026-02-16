# Monthly-Budget-Calculator

This is a simple command-line Python application that helps users calculate their monthly budget.
It collects income and expense details, calculates savings or overspending, and provides a summary including:

Total expenses
Remaining income
Spending percentage
Highest spending category
This project is beginner-friendly and useful for understanding Python basics like:
input() and print()
Variables
Arithmetic operations
Conditional statements
Basic calculations

🚀 Features
Takes user name input and greets them
Accepts monthly income
Tracks expenses across multiple categories:
Food
Groceries
Transportation
Entertainment
Utilities
Other expenses
Calculates:
Total expenses
Remaining income
Spending percentage
Highest expense category
Displays a formatted budget summary

Example:- 

Enter your Name: Rahul
Welcome! Rahul ji
Enter your Monthly income: 30000
Enter your Food cost: 5000
Enter your groceries cost: 4000
Enter your Transportation cost: 3000
Enter your Entertainment cost: 2000
Enter your Utilities cost: 3500
Enter your Other expenses cost: 1500

Great! You saved ₹11000 this month!

========== BUDGET SUMMARY ==========
Total Income:      ₹30000
Total Expenses:    ₹19000
Remaining Budget:  ₹11000
Spending:          63.33%
Top Category:      Food
====================================

🧠 Logic Explanation

All expenses are summed into expenses_total
Remaining income = income - expenses_total
Spending percentage = (expenses_total / income) * 100
The program determines the highest expense category using max()
Conditional statements decide whether the user:
Saved money
Broke even
Overspent

📈 Possible Improvements (Future Updates)
Add input validation (prevent negative numbers)
Store data in a file
Create a graphical interface (Tkinter / Web App)
Add savings goal tracking
Convert to mobile/web version

📚 Learning Outcomes
By building this project, you practice:
Variables and data types
Arithmetic operators
Conditional logic
User input handling
Basic financial calculations
If you want, I can also:
Improve this code to intermediate level
Convert it into an object-oriented version
Help you turn this into a portfolio-ready GitHub project 🚀
