my_list = input().split(" ")
int_list = [int(i) for i in my_list]

number = int(input())
for element in range(number):
    min_element = min(int_list)
    if min_element in int_list:
        int_list.remove(min_element)
for i in int_list:
    print(i, end=", ")