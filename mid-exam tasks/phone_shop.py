list_of_phones = input().split(", ")

while True:
    command = input()

    if command == "End":
        print(", ".join(list_of_phones))
        break

    command = command.split(" ")
    current_command = command[0]

    if current_command != "Bonus":
        current_phone = command[2]
    else:
        current_phone = command[3]

    if current_command == "Add":
        if current_phone not in list_of_phones:
            list_of_phones.append(current_phone)
    elif current_command == "Remove":
        if current_phone in list_of_phones:
            list_of_phones.remove(current_phone)
    elif current_command == "Bonus":
        current_phones = current_phone.split(":")
        if current_phones[0] in list_of_phones:
            index = current_phones.index(current_phones[0])
            list_of_phones.insert(index + 2, current_phones[1])
    elif current_command == "Last":
        if current_phone in list_of_phones:
            list_of_phones.remove(current_phone)
            list_of_phones.append(current_phone)


