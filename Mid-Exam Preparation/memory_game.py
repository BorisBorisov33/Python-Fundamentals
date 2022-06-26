# elements = list(map(int, input().split()))
elements = input().split()
counter_moves = 0
while True:
    command = input()
    if command == "end":
        if len(elements) == 0:
            print(f"You have won in {counter_moves} turns!")
            break
        else:
            print(f"Sorry you lose :( \n"
                  f"{elements}")
            break

    data = command.split()
    current_element_one = int(data[0])
    current_element_two = int(data[1])

    if elements[current_element_one] == elements[current_element_two]:
        counter_moves += 1
        # print(elements[current_element_one])
        # print(elements[current_element_two])
        print(f"Congrats! You have found matching elements - {elements[current_element_two]}!")
        if elements[current_element_one] == str and elements[current_element_two] == str:
            elements.remove(current_element_one)
            elements.remove(current_element_two)
        else:
            elements = [num for num in elements if num != elements[current_element_two]]
            # print(elements)

    elif (current_element_one < 0 or current_element_one > len(elements)) or (
            current_element_two < 0 or current_element_two > len(elements)):
        counter_moves += 1
        middle_element = len(elements) // 2
        elements.insert(middle_element, f"-{counter_moves}a")
        elements.insert(middle_element, f"-{counter_moves}a")
        print(f"Invalid input! Adding additional elements to the board")
        # print(elements)
    elif current_element_one == current_element_two:
        counter_moves += 1
        middle_element = len(elements) // 2
        elements.insert(middle_element, f"-{counter_moves}a")
        elements.insert(middle_element, f"-{counter_moves}a")
        print(f"Invalid input! Adding additional elements to the board")

    elif elements[current_element_two] != elements[current_element_two]:
        counter_moves += 1
        print(f"Try again!")
