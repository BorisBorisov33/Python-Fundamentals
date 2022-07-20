first_String = input()
second_string = input()
while first_String in second_string:
    second_string = second_string.replace(first_String, "")

print(second_string)
