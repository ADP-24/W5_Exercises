pay_rate = float(input("Enter your pay rate (in dollars per hour): "))
hours_worked = float(input("Enter the number of hours worked: "))
filling_status = input("Enter your filling status (single or joint): ").strip().lower()

if hours_worked > 40:
    regular_hours = 40
    overtime_hours = hours_worked - regular_hours
    total_earnings = (regular_hours * pay_rate) + (overtime_hours * pay_rate * 1.5)
else:
    total_earnings = hours_worked * pay_rate

weeks_per_year = 52
annual_gross_pay = total_earnings * weeks_per_year

if filling_status == "single":
    if annual_gross_pay < 12000:
        tax_rate = 0.05
    elif 12000 <= annual_gross_pay <= 24999.99:
        tax_rate = 0.10
    elif 25000 <= annual_gross_pay <= 74999.99:
        tax_rate = 0.15
    elif annual_gross_pay < 75000:
        tax_rate = 0.20
    else:
        tax_rate = 0.20

if filling_status == "joint":
    if annual_gross_pay < 12000:
        tax_rate = 0.00
    if 12000 <= annual_gross_pay <= 24999.99:
        tax_rate = 0.06
    if 25000 <= annual_gross_pay <= 74999.99:
        tax_rate = 0.11
    if annual_gross_pay < 75000:
        tax_rate = 0.20
    else:
        tax_rate = 0.20
else:
    print("Invalid filing status. Please enter 'single' or 'joint'.")

weekly_tax_withheld = total_earnings * tax_rate
net_weekly_income = total_earnings - weekly_tax_withheld


annual_tax = annual_gross_pay * tax_rate
net_income = annual_gross_pay - annual_tax

print(f"Weekly Earnings: ${total_earnings: .2f}")
print(f"Weekly tax withheld: ${weekly_tax_withheld:.2f}")
print(f"Net Weekly Income: ${net_weekly_income:.2f}")
print(f"Estimated Annual Gross Pay: $ {annual_gross_pay:.2f}")
print(f"Tax Rate: {tax_rate * 100}%")
print(f"Annual Tax: ${annual_tax:.2f}")
print(f"Net Income after tax: ${net_income:.2f}")