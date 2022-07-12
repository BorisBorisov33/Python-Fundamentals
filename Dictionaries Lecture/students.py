# information_dict = {}
# command = input().split(":")
# while "_" not in command[0] or command[0] == information_dict.keys():
#     name = command[0]
#     student_id = command[1]
#     course = command[2]
#     if course not in information_dict:
#         information_dict[course] = [name, student_id]
#     else:
#         information_dict[course].append(name)
#         information_dict[course].append(student_id)
#
#     command = input().split(":")
#
# print(information_dict)