sum_without_taxes = 0
price_per_product_after_tax = 0
taxes_20_percent = 0

while True:
    command = input()
    if command == "special":
        price_per_product_after_tax = 0.9 * price_per_product_after_tax
        break
    elif command == "regular":
        pass
        break

    price_without_taxes = float(command)

    if price_without_taxes < 0:
        print('Invalid price!')
        continue

    sum_without_taxes += price_without_taxes

    taxes_20_percent = 0.2 * sum_without_taxes
    price_per_product_after_tax = sum_without_taxes + taxes_20_percent

if price_per_product_after_tax == 0:
    print('Invalid order!')
else:
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {sum_without_taxes:.2f}$"
          f"\nTaxes: {taxes_20_percent:.2f}$\n-----------\
          \nTotal price: {price_per_product_after_tax:.2f}$")
