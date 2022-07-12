number_of_students = int(input())
academy_dict = {}

for student in range(number_of_students):
    name = input()
    grade = float(input())

    if name not in academy_dict:
        academy_dict[name] = [grade]
    else:
        academy_dict[name].append(grade)

academy_dict = {key: val for key, val in academy_dict.items() if
                sum(academy_dict[key]) / len(academy_dict[key]) >= 4.5}

aver_dict = {}
for name in academy_dict.keys():
    aver_dict[name] = float(sum(academy_dict[name]) / len(academy_dict[name]))

for name, average_grade in aver_dict.items():
    print(f"{name} -> {average_grade:.2f}")
