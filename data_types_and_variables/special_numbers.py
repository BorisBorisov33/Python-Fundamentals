number = int(input())

sum_digits = 0
# print(number[0])
for number in range(1, number + 1):
    number = str(number)
    for digit in number:
        if len(number) > 1:
            sum_digits += int(digit)
            if sum_digits% 5 ==0 or sum_digits% 11==0 or sum_digits % 7 ==0:
                print(f"{number} -> True")
            # else:
                # print(f"{number} -> False")

        else:
            if int(number) % 5 == 0:
                print(f"{number} -> True")
            elif int(number) % 7 == 0:
                print(f"{number} -> True")
            elif int(number) % 11 == 0:
                print(f"{number} -> True")
            else:
                print(f"{number} -> False")

