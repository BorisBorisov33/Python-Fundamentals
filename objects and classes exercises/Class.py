class Class:
    __students_count = 22
    students = []
    grades = []

    def __init__(self, name):
        self.name = name

    def add_student(self, name: str, grade: float):
        if Class.__students_count > 0:
            self.students.append(name)
            self.grades.append(grade)
            Class.__students_count -= 1

    def get_average_grade(self):
        sum_grades = sum(self.grades)
        average_grade = sum_grades / len(self.grades)
        return f"{average_grade:.2f}"

    def __repr__(self):
        string_to_return = ''
        string_to_return += f'The students in {self.name}:'
        string_to_return += f" {', '.join(self.students)}.\n"
        string_to_return += f'Average grade: {Class.get_average_grade(self)}'
        return string_to_return
