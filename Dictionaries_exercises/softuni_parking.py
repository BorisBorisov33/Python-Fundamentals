parking_dict = {}
number_of_users = int(input())
command = input().split()
for current_user in range(number_of_users):
    command_register_or_not = command[0]
    username = command[1]

    if command_register_or_not == "register":
        licence = command[2]
        if username in parking_dict.keys():
            print(f"ERROR: already registered with plate number {parking_dict[username]}")
        else:
            parking_dict[username] = licence
            print(f"{username} registered {licence} successfully")
    elif command_register_or_not == "unregister":
        if username not in parking_dict.keys():
            print(f"ERROR: user {username} not found")
        else:
            del parking_dict[username]
            print(f"{username} unregistered successfully")

    if current_user == number_of_users-1:
        break
    command = input().split()

for username, licence in parking_dict.items():
    print(f"{username} => {licence}")
