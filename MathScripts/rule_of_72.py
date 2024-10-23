interest_rate = 5
savings_account = 2000

years_to_double = 72 / interest_rate

print("At a" , str(interest_rate) + "% interest rate", 
      "your savings account will be worth", str(savings_account * 2),
      "in" , format(years_to_double, ".2f") , "years.")