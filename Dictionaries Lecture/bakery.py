# example 1
food_line = input().split()
bakery_dict = {}
for i in range(0, len(food_line), 2):
    bakery_dict[food_line[i]] = int(food_line[i + 1])
print(bakery_dict)

# # example 2
# products_dict = {food_line[i]: int(food_line[i + 1]) for i in range(0, len(food_line), 2)}
# print(products_dict)
