import collections
from locale import _grouping_intervals

import pandas.core.groupby

from leson2.student import Student

list = []

list.append(Student("Ivan", 'Ivanov', '2001', 'PINZH-20', '2', [6, 4, 8, 10, 5]))
list.append(Student("Avan", 'Ivanov', '2001', 'PINZH-20', '2', [6, 4, 8, 10, 5]))
list.append(Student('Sergey', "Sergeevich", '2001', 'PINZH-20', '2', [8, 8, 6, 6, 8]))
list.append(Student('Ivan', 'Ivanov', '2002', 'PINZH-19', '3', [8, 3, 7, 6, 4]))

# studentList.sort(key= student: student.first_name, reverse=True)

def sorting(studentList):
    studentList = sorted(studentList, key=lambda student: (student.course, student.first_name, student.last_name),
                         reverse=False)
    for studetn in studentList:
        print(studetn)

def group_list(lst):
    df = pandas.DataFrame(lst)
    edn = df.groupby(group_keys= lambda student: student.group_name)
    print(edn)

sorting(list)

print()

group_list(list)



