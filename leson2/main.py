import collections

import pandas.core.groupby

from leson2 import student
from leson2.student import Student

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
    map_student = dict.fromkeys([stud.group_name for stud in lst])

    for student in lst:
        key = student.group_name
        if( map_student[key] == None):
            map_student[key] = [student]
        else:
            map_student[key].append(student)


    for s in map_student:
        print(s)







    print(map_student)

sorting(list_s)

print()

group_list(list_s)



