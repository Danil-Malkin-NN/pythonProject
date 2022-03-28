import collections

import numpy

from leson2.student import Student
from itertools import groupby
from pprint import pprint

list_s = []

list_s.append(Student("Ivan", 'Ivanov', '2001', 'PINZH-20', '2', [6, 4, 8, 10, 5]))
list_s.append(Student("Avan", 'Ivanov', '2001', 'PINZH-20', '2', [6, 4, 8, 10, 5]))
list_s.append(Student('Sergey', "Sergeevich", '2001', 'PINZH-20', '2', [8, 8, 6, 6, 8]))
list_s.append(Student('Ivan', 'Ivanov', '2002', 'PINZH-19', '3', [8, 3, 7, 6, 4]))


# studentList.sort(key= student: student.first_name, reverse=True)

def sorting(studentList):
    studentList = sorted(studentList, key=lambda student: (student.course, student.first_name, student.last_name),
                         reverse=False)
    for studetn in studentList:
        print(studetn)


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


sorting(list_s)

print()

map_s = group_list(list_s)
sum_marks(map_s)

