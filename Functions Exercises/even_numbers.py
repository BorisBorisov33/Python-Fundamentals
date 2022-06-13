# numbers_as_string = input().split()

numbers_as_digit = [int(i) for i in input().split()]

is_even = lambda x: x % 2 == 0

result = list(filter(is_even, numbers_as_digit))
print(result)
