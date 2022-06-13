def is_perfect(some_number):
    sum_div = 0
    for divisor in range(1, some_number):
        if some_number % divisor == 0:
            sum_div += divisor
    if some_number == sum_div:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(is_perfect(number))
