#This help users to calculate their monthly savings.
monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))
  #To calculate their monthly savings
monthly_savings = monthly_income - monthly_expenses
print("Your monthly savings are $", monthlySavings)
#projected annual savings
projectedAnnualSavings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Projected savings after one year, with interest, is: $",projectedAnnualSavings)

