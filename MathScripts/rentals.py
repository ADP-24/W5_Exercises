import math

number_of_tourists = 38

vans_needed =  math.ceil(number_of_tourists/15)

total_cost = vans_needed * 250

cost_per_person = total_cost/number_of_tourists if number_of_tourists > 0 else 0

print(f"Total cost per person would be ${cost_per_person:.2f}")
print(f"The number of vans needed are {vans_needed}")
print(f"The total cost of the vans were ${total_cost: .2f}")