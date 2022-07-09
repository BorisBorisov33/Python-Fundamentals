resources = {}

while True:
    current_resource = input()
    if current_resource == "stop":
        break

    quantity = int(input())
    if current_resource not in resources:
        resources[current_resource] = 0

    resources[current_resource] += quantity
    # another way of writing the previous four lines
    #     if current_resource not in resources:
    #       resources[current_resource] = quantity
    #     else:
    #       resources[current_resource] += quantity

for resource, value_of_resource in resources.items():
    print(f"{resource} -> {value_of_resource}")
