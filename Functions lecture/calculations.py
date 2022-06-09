

def calculation_func(number_a, number_b, operation):
    if operation == "multiply":
        return int(number_a * number_b)
    elif operation == "divide":
        return int(number_a / number_b)
    elif operation == "add":
        return int(number_a + number_b)
    elif operation == "subtract":
        return int(number_a - number_b)


type_of_operation = input()
first_num = int(input())
second_num = int(input())
result = calculation_func(first_num, second_num,type_of_operation)
print(result)
