from datetime import datetime

def get_greeting(hour):

    if hour < 0 or hour > 23:
        return "Invalid hour. Please enter a value between 0 and 23"
    elif 23 <= hour or hour < 4:
        return "What are you doing up so late??"
    elif hour < 10:
        return "Good Morning"
    elif hour < 17:
        return "Good day!"
    else:
        return "Good evening!"
    
test_hours = [13, 2, 4]

for hour in test_hours:
    greeting = get_greeting(hour)
    print(f"Hour {hour}: {greeting}")

current_hour = datetime.now().hour

greeting = get_greeting(current_hour)

print(f"current hour: {current_hour}")
print(f"Greeting: {greeting}")