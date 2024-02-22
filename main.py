# This program calculates an employees' adjusted take-home pay

# Title, Unit number
print("UNIT TEST #2")


# Input Statements
stateTaxPercent = 6.5/100
fedTaxPercent = 28.0/100
deductionPercent = 2.5/100
numDependants = 6
salary = 30000.00


# Deduction Calculations
stateTax = salary * ( stateTaxPercent)
fedTax = salary * (fedTaxPercent)
dependentDeduction = numDependants * (salary * deductionPercent) 


# Totals
totalWithholding = stateTax + fedTax + dependentDeduction
takeHomePay = salary - totalWithholding


# Output Statements
print("State Tax: $" +str(stateTax))
print("Federal Tax: $" +str(fedTax))
print("Dependants: $" +str(dependentDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
