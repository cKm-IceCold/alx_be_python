#This help users to calculate their monthly savings.
monthlyIncome = int(input("Enter your monthly income:"))
totalMonthlyExpense = int(input("Enter your total monthly expenses:"))
  #To calculate their monthly savings
monthlySavings = monthlyIncome - totalMonthlyExpense
print("Your monthly savings are $", monthlySavings)
#projected annual savings
projectedAnnualSavings = monthlySavings * 12 + (monthlySavings * 12 * 0.05)
print("Projected savings after one year, with interest, is: $",projectedAnnualSavings)

