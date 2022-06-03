my_list = input().split()
opposite_numbers = []
for element in my_list:
    # print(type(element))
    opposite_numbers.append(-int(element))

print(opposite_numbers)