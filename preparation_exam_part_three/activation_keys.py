key = input()

while True:
    command = input().split(">>>")
    current_command = command[0]

    if current_command == "Generate":
        print(f"Your activation key is: {key}")
        break

    elif current_command == "Slice":
        key = key[:int(command[1])] + key[int(command[2]):]
        print(key)
    elif current_command == "Flip":
        if command[1] == "Upper":
            key = key[:int(command[2])] + key[int(command[2]):int(command[3])].upper() + key[int(command[3]):]
        else:
            key = key[:int(command[2])] + key[int(command[2]):int(command[3])].lower() + key[int(command[3]):]
        print(key)
    elif current_command == "Contains":
        if command[1] in key:
            print(f"{key} contains {command[1]}")
        else:
            print("Substring not found!")

