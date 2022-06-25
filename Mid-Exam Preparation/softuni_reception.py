first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
count_student = int(input())

hours_needed = 0
responded_students = first_employee + second_employee + third_employee

while count_student > 0:

    hours_needed += 1
    count_student -= responded_students
    if hours_needed % 4 == 0:
        hours_needed += 1

    if count_student <= responded_students:
        hours_needed += 1
        if hours_needed % 4 == 0:
            hours_needed += 1
        break

print(f"Time needed: {hours_needed}h.")
