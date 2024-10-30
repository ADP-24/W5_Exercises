bank_balance = 1000.00
savings_goal = 5000.00
weekly_savings = 200.00

while bank_balance < savings_goal:
    bank_balance += weekly_savings

    if bank_balance >= savings_goal * 0.5 and bank_balance < savings_goal * 0.75:
        print(f"Almost there! This week my balance is up to ${bank_balance:.2f}.")

    elif bank_balance >= savings_goal * 0.75 and bank_balance < savings_goal:
        print(f"So close! After treating myself, my balance is up to ${bank_balance}.")

    else:
        print(f"This week my balance increased to ${bank_balance:.2f}.")

print(f"Goal met! My current balance is ${bank_balance:.2f}.")