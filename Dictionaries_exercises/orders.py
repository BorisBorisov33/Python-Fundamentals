dict_store = {}

command = input().split()

while command[0] != "buy":
    product, price, quantity = command

    if product not in dict_store.keys():
        #                         0           1              2
        dict_store[product] = [float(price), int(quantity)]
        total_price = int(quantity) * float(price)
        dict_store[product].append(total_price)

    else:
        dict_store[product][1] += int(quantity)
        if float(price) != dict_store[product][0]:
            dict_store[product][0] = price
            total_price = dict_store[product][1] * float(price)
            dict_store[product][2] = total_price

    command = input().split()

for key in dict_store.keys():
    print(f"{key} -> {dict_store[key][2]:.2f}")

# dict_store[product] = [price, quantity, total_price]
# update the quantity and the price as requested in the task 
