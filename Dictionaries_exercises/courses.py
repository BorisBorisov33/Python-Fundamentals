courses_dict = {}
command = input().split(" : ")
while command[0] != "end":

    course_name, student_name = command
    if course_name not in courses_dict:
        courses_dict[course_name] = [student_name]
    else:
        courses_dict[course_name].append(student_name)

    command = input().split(" : ")


for key in courses_dict:
    print(f"{key}: {len(courses_dict[key])}")
    for value in courses_dict[key]:
        print(f"-- {value}")
