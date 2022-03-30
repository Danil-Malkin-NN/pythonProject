from leson2.student import Student
from itertools import groupby
from pprint import pprint

list_s = []

list_s.append(Student("Ivan", 'Ivanov', '2001', 'PINZH-20', '2', [6, 4, 8, 10, 5]))
list_s.append(Student("Avan", 'Ivanov', '2001', 'PINZH-20', '2', [6, 4, 8, 10, 5]))
list_s.append(Student('Sergey', "Sergeevich", '2001', 'PINZH-20', '2', [8, 8, 6, 6, 8]))
list_s.append(Student('Ivan', 'Ivanov', '2002', 'PINZH-19', '3', [8, 3, 7, 6, 4]))


def sorting(studentList):
    studentList = sorted(studentList, key=lambda student: (student.course, student.first_name, student.last_name),
                         reverse=False)
    for studetn in studentList:
        print(studetn)
    return studentList


def group_list(lst):
    map_student = {k: list(v) for k, v in groupby(lst, key=lambda x: x.group_name)}
    return map_student


def average(lst):
    return sum(lst) / len(lst)


def sum_marks(map_student):
    for key, value in map_student.items():
        best_student = [None, 0]
        for stud in value:
            a = average(stud.marks_list)
            if (best_student[1] < a):
                best_student[0] = stud
                best_student[1] = a
        print(f'''Best student in group {key} is {best_student[0]}''')


print("Сортировка по курсу, имени и фамилии")
list_s = sorting(list_s)
print(list_s)

map_s = group_list(list_s)
pprint("Поиск лучшего студента по всем оценкам")
sum_marks(map_s)

print()
print("Поиск младшего студента")
print(max(list_s, key=lambda stud: int(stud.year_of_birthday)))

print()
print("Поиск старшего студента")
print(min(list_s, key=lambda stud: int(stud.year_of_birthday)))

print()
print("Средний бал для каждого предмета каждой группы")


def search_average_score_by_matrix(matrix):
    res = [round(average(x), 2) for x in zip(*matrix)]
    print(res)


def search_gpa_by_students_group(groups_of_students):
    for s, value in groups_of_students.items():
        matrix_of_grades = [stud.marks_list for stud in value]
        print('\nGPA for ' + s + ' group')
        search_average_score_by_matrix(matrix_of_grades)


search_gpa_by_students_group(map_s)
