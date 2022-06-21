def lift_func(people_in_queue, current_state_of_the_lift):
    for coupe in range(len(current_state_of_the_lift)):
        if people_in_queue > 3:
            current_number_of_people = abs(4 - int(current_state_of_the_lift[coupe]))
            people_in_queue -= current_number_of_people
            current_state_of_the_lift[coupe] = current_number_of_people

        else:
            current_state_of_the_lift[coupe] += people_in_queue
            people_in_queue = 0
    if people_in_queue > 0:
        print(f"There isn't enough space! {people_in_queue} people in a queue!")
    elif sum(current_state_of_the_lift) != len(current_state_of_the_lift) * 4:
        print(f"The lift has empty spots!")

    return ' '.join([str(num) for num in current_state_of_the_lift])


people = int(input())
lift_condition = [int(x) for x in input().split()]
print(lift_func(people, lift_condition))
