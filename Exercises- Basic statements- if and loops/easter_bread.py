budget = float(input())
price_per_1kg_flour = float(input())
price_per_pack_eggs = 0.75 * price_per_1kg_flour
price_per_1_liter_milk = 1.25 * price_per_1kg_flour
price_per_250ml_milk = price_per_1_liter_milk / 4
counter_loaf = 0
coloured_eggs = 0
one_loaf_price = price_per_pack_eggs + price_per_1kg_flour + price_per_250ml_milk
total_price = 0


while budget > 0:
    if budget < one_loaf_price:
        break
    budget -=  one_loaf_price

    counter_loaf += 1
    coloured_eggs += 3
    if counter_loaf % 3 == 0:
        coloured_eggs -= (counter_loaf - 2)

print(f"You made {counter_loaf} loaves of Easter bread! Now you have {coloured_eggs} eggs and {budget:.2f}BGN left.")