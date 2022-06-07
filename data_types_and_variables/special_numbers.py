number = int(input())
for number in range(1, number + 1):
    if number % 10 + number // 10 == 5 or number % 10 + number // 10 == 7 or number % 10 + number // 10 == 11:
        print(f"{number} -> True")
    else:
        print(f"{number} -> False")

