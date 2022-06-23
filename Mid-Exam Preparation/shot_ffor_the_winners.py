def shoot_the_target(index_function, list_of_targets):
    shot_target=[]
    if index_function < len(list_of_targets):
        shot_target.append(list_of_targets[index_function])
        for number in targets:
            if number not in shot_target:
                if list_of_targets[index_function] < number:
                    number -= list_of_targets[index_function]
                else:
                    number += list_of_targets[index_function]

            list_of_targets[index_function]=-1

targets = list(map(int, input().split()))

while True:
    command = input()
    if command == "End":
        print(f"Shot targets: {targets.count(-1)} -> {' '.join(str(num) for num in targets)}")
        break

    index = int(command)
    shoot_the_target(index, targets)
