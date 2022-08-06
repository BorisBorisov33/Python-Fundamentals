stops = input()

command = input().split(':')
# destination = {}
while True:
    if command[0] == "Travel":
        break
    if command[0] == "Add Stop":
        if int(command[1]) < len(stops):
            index = int(command[1])
            stops = stops[:index] + command[2] + stops[index:]
            print(stops)
    elif command[0] == "Remove Stop":
        if int(command[1]) < len(stops) and int(command[2]) < len(stops):
            stops = stops[0:int(command[1])] + stops[int(command[2]) + 1:]
            print(stops)
    elif command[0] == "Switch":
        if command[1] in stops:
            # index = stops.index(command[1])
            stops = stops.replace(command[1], command[2])
            print(stops)
    else:
        stops = stops
    command = input().split(':')

print(f"Ready for world tour! Planned stops: {stops}")
