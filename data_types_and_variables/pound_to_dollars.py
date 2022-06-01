# First way of solving the task

# pounds = int(input())
# dollars = pounds * 1.31
# print(f'{dollars:.3f}')
#

# Second way of solving the task
from forex_python.converter import CurrencyRates

amount = int(input("Enter the number of pounds:"))
c = CurrencyRates()
current_Rate = c.get_rate("GBP", 'USD')
result = current_Rate * amount
print(f"Your sum in dollars is: {result:.3f}")
