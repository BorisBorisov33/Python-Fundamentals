number = int(input())
word = input()
my_list = []
my_list_filtered = []
for string in range(number):
    current_string = input()
    my_list.append(current_string)
    if word not in current_string:
        continue
    my_list_filtered.append(current_string)

print(my_list)
print(my_list_filtered)
