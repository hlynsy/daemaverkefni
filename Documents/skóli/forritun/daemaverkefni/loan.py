loan_amount = float(input("Input the cost of the item in $: "))

while loan_amount >= 2500:
    print("Error, Loan cannot be larger than 2500 $")
    loan_amount = float(input("Input the loan amount in $ "))

if loan_amount <= 1000:
    interest_rate = 0.015
else:
    interest_rate = 0.02

remaining_debt = loan_amount
months = 0
interest_paid = 0.00
monthly_payment = 0.00
total_interest_paid = 0.00

while remaining_debt > 50.00:
    months += 1
    interest_paid = remaining_debt * interest_rate
    monthly_payment = 50.00
    paid_debt = 50.00 - interest_paid
    total_interest_paid += interest_paid
    remaining_debt = remaining_debt - paid_debt
    print("Month: " + str(months) + " Payment: " + str(monthly_payment) + " Interest paid: " + str(round(interest_paid, 2)) + " Remaining debt: " + str(round(remaining_debt, 2)))


months += 1
interest_paid = remaining_debt * interest_rate
monthly_payment = remaining_debt+interest_paid
total_interest_paid += interest_paid
remaining_debt = 0.00
print("Month: " + str(months) + " Payment: " + str(round(monthly_payment, 2)) + " Interest paid: " + str(round(interest_paid, 2)) + " Remaining debt: " + str(round(remaining_debt, 2)))
print("\nNumber of months: " + str(months))
print("Total interest paid: " + str(round(total_interest_paid, 2)))