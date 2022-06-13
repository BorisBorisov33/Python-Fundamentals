def calculate_factorial(some_number):
    sum_fact = 0
    for factorial in range(1, some_number):
        some_number *= factorial
    return some_number


first_number = int(input())
second_number = int(input())

first_num_factorial = calculate_factorial(first_number)
second_num_factorial = calculate_factorial(second_number)
result = first_num_factorial / second_num_factorial
print(f"{result:.2f}")
