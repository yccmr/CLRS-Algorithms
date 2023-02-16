class STU:
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade

    def get_grade(self):
        return self.__grade

    def change_grade(self, new_grade):
        self.__name = new_grade

    def __str__(self):
        return "({}: {})".format(self.__name, self.__grade)

    def __eq__(self, other):
        return self.__grade == other.get_grade()

    def __lt__(self, other):
        return self.__grade < other.get_grade()

    def __gt__(self, other):
        return self.__grade > other.get_grade()

