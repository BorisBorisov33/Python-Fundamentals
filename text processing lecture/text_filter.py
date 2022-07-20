first_String = input().split(", ")
second_string = input()

for el in first_String:
    while el in second_string:
        second_string = second_string.replace(el, "*" * len(el))

print(second_string)
