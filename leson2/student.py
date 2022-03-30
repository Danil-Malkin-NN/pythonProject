class Student:

    def __init__(self, f_name, l_name, year, group, course, marks):
        self.first_name = f_name
        self.last_name = l_name
        self.year_of_birthday = year
        self.group_name = group
        self.course = course
        self.marks_list = marks

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name + " " + self.year_of_birthday + " " + self.group_name + " cours " + self.course + " Marks: " + "/".join(str(x) for x in self.marks_list)

    def __repr__(self) -> str:
        return self.__str__()


