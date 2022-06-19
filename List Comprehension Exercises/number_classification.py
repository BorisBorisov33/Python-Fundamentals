def positive_number(numbers):
    return [number for number in numbers if int(number) >= 0]


def negative_number(numbers):
    return [number for number in numbers if int(number) < 0]


def even_numbers(numbers):
    return [number for number in numbers if int(number) % 2 == 0]


def odd_numbers(numbers):
    return [number for number in numbers if int(number) % 2 != 0]


numbers_as_string = input().split(", ")

print(f"Positive: {', '.join(positive_number(numbers_as_string))}")
print(f"Negative: {', '.join(negative_number(numbers_as_string))}")
print(f"Even: {', '.join(even_numbers(numbers_as_string))}")
print(f"Odd: {', '.join(odd_numbers(numbers_as_string))}")


# print(f"Negative: {', '.join(str(number) for number in numbers_as_string if int(number) < 0)}")
# print(f"Even: {', '.join(str(number) for number in numbers_as_string if int(number) % 2 == 0)}")
# print(f"Odd: {', '.join(str(number) for number in numbers_as_string if int(number) % 2 != 0)}")
