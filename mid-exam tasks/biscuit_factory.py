import math

number_of_biscuits_per_day = int(input())
count_of_the_workers = int(input())
number_of_biscuits_for_30_days_other = int(input())

produce_per_day = number_of_biscuits_per_day * count_of_the_workers  # 20 days
produce_per_every_third_day = 0.75 * produce_per_day  # 10 days

product_for_twenty_days = 20 * produce_per_day
product_for_ten_days = 10 * math.floor(produce_per_every_third_day)

result_of_my_factory = product_for_twenty_days + product_for_ten_days
difference = result_of_my_factory - number_of_biscuits_for_30_days_other

percentage = (difference / number_of_biscuits_for_30_days_other) * 100

print(f"You have produced {result_of_my_factory} biscuits for the past month.")

if result_of_my_factory > number_of_biscuits_for_30_days_other:
    print(f"You produce {abs(percentage):.2f} percent more biscuits.")
else:
    print(f"You produce {abs(percentage):.2f} percent less biscuits.")
