names_list = input().split(", ")
result = sorted(names_list, key=lambda item: (len(item), item), reverse=True)
print(result)
