name = "Irtaza"
age = 29
drinks_coffee = True
salary = 70000.0

print(f"Hello! I am {name}. I am {age} yrs old. I {'do' if drinks_coffee else 'do not'} drinks coffee. And i earn around {salary} per month")

retirement_age = 60
coffee_price = 150.0
cups_per_day = 3
days_in_week = 7

print(f"Years left till retirement is {retirement_age - age}")
print(f"Weekly coffee budget: Rs{coffee_price * cups_per_day * days_in_week}")