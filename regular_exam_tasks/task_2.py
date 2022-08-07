import re

number = int(input())

for _ in range(number):
    data = input()
    searched_pattern = r'\!([A-Z][a-z]{2,})\!\:\[([A-Za-z]{8,})\]'

    matches = re.match(searched_pattern, data)

    if matches:
        first_string = matches.group(1)
        second_string = matches.group(2)

        list_nums = []
        for letter in second_string:
            list_nums.append(ord(letter))
        print(f"{first_string}: {' '.join(str(element) for element in list_nums)}")
    else:
        print("The message is invalid")




