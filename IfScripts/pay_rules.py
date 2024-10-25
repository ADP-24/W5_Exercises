pay_rate = float(input("Enter your pay rate (in dollars per hour): "))
hours_worked = float(input("Enter the number of hours worked: "))

if hours_worked > 40:
    regular_hours = 40
    overtime_hours = hours_worked - regular_hours
    total_earnings = (regular_hours * pay_rate) + (overtime_hours * pay_rate * 1.5)
else:
    total_earnings = hours_worked * pay_rate

print(f"Total Earnings: ${total_earnings: .2f}")