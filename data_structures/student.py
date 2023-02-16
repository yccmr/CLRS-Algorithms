class STU:
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade

    def change_grade(self, new_grade):
        self.__name = new_grade

    def __str__(self):
        return "({}: {})".format(self.__name, self.__grade)

