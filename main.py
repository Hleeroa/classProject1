class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade()

    def average_grade(self):
        all_grades = []
        i = 0
        for pair in self.grades.values():
            for grade in pair:
                all_grades.append(grade)
        for grades in all_grades:
            i += grades
        if len(all_grades) == 0:
            average = 'у Вас пока не оценок'
        else:
            average = i / len(all_grades)
        return average

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return 'Имя: ' + self.name + '\nФамилия: ' + self.surname + '\nСредняя оценка за домашние задания: ' + str(self.average_grade()) + '\nКурсы в процессе изучения: ' + ", ".join(self.courses_in_progress) + '\nЗавершенные курсы: ' + ", ".join(self.finished_courses)

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grade()

    def average_grade(self):
        all_grades = []
        i = 0
        for pair in self.grades.values():
            for grade in pair:
                all_grades.append(grade)
        for grades in all_grades:
            i += grades
        if len(all_grades) == 0:
            average = 'У Вас пока не оценок'
        else:
            average = i / len(all_grades)
        return average

    def __str__(self):
        return 'Имя: ' + self.name + '\nФамилия: ' + self.surname + '\nСредняя оценка за лекции: ' + str(self.average_grade())

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return 'Имя: ' + self.name + '\nФамилия: ' + self.surname


def all_st_average(people, course_name):
    if not isinstance(people, list):
        return "Not list"
    all_grades = []
    for person in people:
        if course_name in person.grades.keys():
            av = sum(person.grades[course_name])/len(person.grades[course_name])
            all_grades.append(av)
    if not all_grades:
        return "По такому курсу ни у кого нет оценок"
    return sum(all_grades)/len(all_grades)


def all_lc_average(mentors, course_name):
    if not isinstance(mentors, list):
        return "Not list"
    all_grades = []
    for mentor in mentors:
        if course_name in mentor.grades.keys():
            av = sum(mentor.grades[course_name])/len(mentor.grades[course_name])
            all_grades.append(av)
    if not all_grades:
        return "По такому курсу ни у кого нет оценок"
    return sum(all_grades)/len(all_grades)


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python', 'Python - введение в программирование', 'Adobe Photoshop']
print(cool_reviewer)
print('\n')

some_reviewer = Reviewer('Same', 'Bro')
some_reviewer.courses_attached += ['Java', 'Bold management']
print(some_reviewer)
print('\n')

some_student = Student('Evance', 'Hanson', 'gender')
some_student.courses_in_progress += ['Java', 'Adobe Photoshop']
some_student.finished_courses += ['Python - введение в программирование']
cool_reviewer.rate_hw(some_student, 'Adobe Photoshop', 10)
cool_reviewer.rate_hw(some_student, 'Adobe Photoshop', 9)
some_reviewer.rate_hw(some_student, 'Java', 7)
some_reviewer.rate_hw(some_student, 'Java', 5)
print(some_student)
print('\n')

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Bold management']
best_student.courses_in_progress += ['Java']
some_reviewer.rate_hw(best_student, 'Bold management', 10)
some_reviewer.rate_hw(best_student, 'Bold management', 9)
some_reviewer.rate_hw(best_student, 'Bold management', 10)
some_reviewer.rate_hw(best_student, 'Java', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
print(best_student)
print('\n')

same_lecturer = Lecturer('Square', 'Look')
same_lecturer.courses_attached += ['Python', 'Python - введение в программирование', 'Bold management']
same_lecturer.courses_attached += ['Adobe Photoshop']
some_student.rate_hw(same_lecturer, 'Adobe Photoshop', 9)
best_student.rate_hw(same_lecturer, 'Python', 10)
best_student.rate_hw(same_lecturer, 'Bold management', 8)
print(same_lecturer)
print('\n')

best_lecturer = Lecturer('Doctor', 'Triangle')
best_lecturer.courses_attached += ['Adobe Photoshop']
best_lecturer.courses_attached += ['Java']
some_student.rate_hw(best_lecturer, 'Adobe Photoshop', 10)
some_student.rate_hw(best_lecturer, 'Java', 10)
print(best_lecturer)
print('\n')
print(best_student < some_student)
print('\n')
print(same_lecturer < best_lecturer)
print('\n')
print(all_st_average([best_student, some_student], 'Doctor'))
print('\n')
print(all_st_average([best_student, some_student], 'Java'))
print('\n')
print(all_lc_average([best_lecturer, same_lecturer], 'Adobe Photoshop'))
