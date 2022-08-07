data = input()
while True:
    command = input().split(" ")
    current_command = command[0]

    if current_command == "End":
        break
    if current_command == "Translate":
        character = command[1]
        replacement = command[2]
        data = data.replace(character, replacement)
        print(data)

    elif current_command == "Includes":
        substring = command[1]
        if substring in data:
            print(f"True")
        else:
            print(f"False")

    elif current_command == "Start":
        substring = command[1]
        if data.startswith(substring):
            print(f"True")
        else:
            print(f"False")

    elif current_command == "Lowercase":
        data = data.lower()
        print(data)

    elif current_command == "FindIndex":
        character = command[1]
        index = data.rindex(character)
        print(index)

    elif current_command == "Remove":
        start_index = int(command[1])
        count = int(command[2])
        data = ''.join([data[i] for i in range(len(data)) if i < start_index or i >= start_index + count])
        print(data)
