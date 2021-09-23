
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def lecturer_grade(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in (self.courses_in_progress or self.finished_courses) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return print(f'Ошибка,{self.name} {self.surname} не может оценить лекции {lecturer.surname} по {course}т.к. не ходит на них ')

    def __str__(self):
        result_one = f'Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за домашние задания {middle_grades(list_avarage_grade(self.grades))}\n'
        result_two = f'Курсы в процессе изучения:{self.courses_in_progress}\n Завершенные курсы:{self.finished_courses}'
        return result_one+result_two

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("It is not to compare")
        else:
            return middle_grades(list_avarage_grade(self.grades)) < middle_grades(list_avarage_grade(other.grades))

    def __gt__(self, other):
        if not isinstance(other, Student):
            print("It is not to compare")
        else:
            return middle_grades(list_avarage_grade(self.grades)) > middle_grades(list_avarage_grade(other.grades))


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res_one = f'Имя:{self.name}\nФалилия:{self.surname}\n'
        res_two = f'Средняя оценка за лекции:{middle_grades(list_avarage_grade(self.grades))}'
        return res_one+res_two

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("It is not to compare")
            return
        else:

            return middle_grades(list_avarage_grade(self.grades)) < middle_grades(list_avarage_grade(other.grades))

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print("It is not to compare")
        else:
            return middle_grades(list_avarage_grade(self.grades)) > middle_grades(list_avarage_grade(other.grades))


class Reviewer(Mentor):
    def rev(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result


def middle_grades(list_grades):

    count = len(list_grades)
    summa = 0
    if count != 0:
        for element in range(count):
            summa += list_grades[element]
        result = round(summa/count, 2)
    else:
        result = 'Оценок нет'
    return result


def list_avarage_grade(dict_grades):
    avar_list_grade = []
    for mean in dict_grades.values():
        mean = middle_grades(mean)
        avar_list_grade.append(mean)  # список  всех оценок  #
    return avar_list_grade


def middle_hw_on_course(list_students, subject):
    list_mid_grade_on_course = []

    for stud in range(len(list_students)):

        stud = list_students[stud]
        if subject in stud.grades:
            mid_grade_hw_on_course = middle_grades(stud.grades[subject])
            list_mid_grade_on_course += [mid_grade_hw_on_course]

    result = middle_grades(list_mid_grade_on_course)
    return result


def middle_grade_course(list_mentor, name_course):
    list_all_grades = []
    for key in range(len(list_mentor)):
        list_grades = []
        if name_course in list_mentor[key].grades:

            list_grades += list_mentor[key].grades[name_course]

        list_all_grades += list_grades
    return middle_grades(list_all_grades)

one_lecturer = Lecturer("Александр", "Македонский")
two_lecturer = Lecturer('Федор', 'Конюхов')
three_lecturer = Lecturer('Ваня', 'Пупкин')
one_lecturer.courses_attached = ["История", 'Стратегия',  'Шахматы']
two_lecturer.courses_attached = ["География", "Навигация", "История", 'Python']
three_lecturer.courses_attached = ['Python', 'OOP', 'Шахматы', "История"]

student_one = Student("Александр", "Котиков", "муж")
student_two = Student("Михаил", "Кутузов", "муж")
student_three = Student('Жерик', 'Умников', "муж")

student_one.courses_in_progress = ["История", "География", 'Шахматы']
student_two.courses_in_progress = ["История", "Навигация", 'Python']
student_three.courses_in_progress = ['Python', 'OOP', 'История']

student_one.lecturer_grade(one_lecturer, "Шахматы", 6)

one_reviewer = Reviewer("Асисстент", "1")
one_reviewer.courses_attached = ["История", 'Стратегия',  'Шахматы']

two_reviewer = Reviewer("Ассистент", '2')
two_reviewer.courses_attached = ["Навигация", 'Python', 'География', "История"]

one_reviewer.rev(student_one, "Шахматы", 5)
one_reviewer.rev(student_one, "Шахматы", 5)
one_reviewer.rev(student_one, "История", 6)
one_reviewer.rev(student_one, "История", 6)
one_reviewer.rev(student_one, "Шахматы", 5)
two_reviewer.rev(student_one, "География", 9)
two_reviewer.rev(student_one, "География", 6)
two_reviewer.rev(student_one, "География", 5)

two_reviewer.rev(student_two, "Python", 9)
two_reviewer.rev(student_two, "Python", 5)
two_reviewer.rev(student_two, "Python", 7)
two_reviewer.rev(student_two, "Навигация", 6)
two_reviewer.rev(student_two, "Навигация", 10)
two_reviewer.rev(student_two, "История", 6)
two_reviewer.rev(student_two, "Навигация", 6)
two_reviewer.rev(student_two, "История", 6)
two_reviewer.rev(student_two, "История", 6)

two_reviewer.rev(student_three, "Python", 3)
two_reviewer.rev(student_three, "Python", 6)
two_reviewer.rev(student_three, "Python", 8)
two_reviewer.rev(student_three, "Python", 9)
two_reviewer.rev(student_three, "История", 10)
two_reviewer.rev(student_three, "История", 6)

student_one.lecturer_grade(one_lecturer, "История", 8)
student_one.lecturer_grade(one_lecturer, "Шахматы", 9)
student_two.lecturer_grade(one_lecturer, "История", 7)
student_one.lecturer_grade(one_lecturer, "История", 5)
student_two.lecturer_grade(two_lecturer, "География", 8)
student_two.lecturer_grade(two_lecturer, "История", 1)
student_two.lecturer_grade(two_lecturer, "Python", 3)
student_two.lecturer_grade(two_lecturer, "Python", 2)
student_two.lecturer_grade(three_lecturer, "Python", 8)
student_two.lecturer_grade(three_lecturer, "Python", 5)
student_three.lecturer_grade(three_lecturer, 'Python', 7)
student_three.lecturer_grade(three_lecturer, 'Python', 9)
student_three.lecturer_grade(three_lecturer, 'История', 7)

print(one_lecturer)
print("\n", two_lecturer)
print("\n", three_lecturer)
print("\n", student_one)
print("\n", student_two)
print("\n", student_three)

print("\n", student_one < student_two)

list_stud = [student_one, student_two, student_three]
course_hw = 'Навигация'
mid_grade_hw = middle_hw_on_course(list_stud, course_hw)

print(f'Средняя оценка Д.З. по курсу {course_hw} составляет {mid_grade_hw}')
print("\n")
list_lecturer = [one_lecturer, two_lecturer, three_lecturer]
course = 'Python'

print(f'Средняя оценка лекторов по курсу {course} составляет: {middle_grade_course(list_lecturer, course)}')
