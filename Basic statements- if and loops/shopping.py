budget = int(input())
spent_budget = 0
is_the_budget_spent = False
command = input()
while command != "End":
    price_each_product = int(command)
    spent_budget += price_each_product
    if spent_budget > budget:
        is_the_budget_spent = True
        break

    command = input()

if is_the_budget_spent:
    print(f"You went in overdraft!")
else:
    print(f"You bought everything needed.")