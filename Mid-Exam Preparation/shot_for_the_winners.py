def shoot_the_target(index_function, list_of_targets):
    if index_function < len(list_of_targets):
        saved_number = list_of_targets[index_function]
        list_of_targets[index_function] = -1

        for number in list_of_targets:
            if number != -1:
                if saved_number < number:
                    index_pos = list_of_targets.index(number)
                    number -= saved_number
                    list_of_targets[index_pos] = number
                else:
                    index_neg = list_of_targets.index(number)
                    number += saved_number
                    list_of_targets[index_neg] = number
            else:
                continue
    return list_of_targets


targets = list(map(int, input().split()))

while True:
    command = input()
    if command == "End":
        print(f"Shot targets: {targets.count(-1)} -> {' '.join(str(num) for num in targets)}")
        break

    index = int(command)
    shoot_the_target(index, targets)
