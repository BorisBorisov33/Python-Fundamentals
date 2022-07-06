stock = input().split()
stock_dict = {}
for i in range(0, len(stock), 2):
    stock_dict[stock[i]] = int(stock[i + 1])

items = input().split()

for item in items:
    if item in stock_dict:
        print(f'We have {int(stock_dict[item])} of {item} left')
    else:
        print(f"Sorry, we don't have {item}")

# example = {'nums': {1: 'one', 2: 'two'}, 'letters': {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'},
#            'chars': {'plus': '+', 'minus': '-'}}
#
# for key, value in example.items():
#     for nested_key,nested_value in value.items():
#         print(f'{nested_key}:{nested_value}')
