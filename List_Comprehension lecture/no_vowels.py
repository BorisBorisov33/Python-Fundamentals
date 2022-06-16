text = input()
values = ["a", 'o', 'u', 'e', 'i']
result = [char for char in text if char.lower() not in values]
print(''.join(result))
