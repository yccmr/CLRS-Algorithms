# Implementation of stack

from student import STU


class Stack:
    def __init__(self):
        self.__elements = []

    def push(self, new):
        self.__elements.append(new)

    def pop(self):
        if self.is_empty():
            print("Error: Cannot pop from an empty stack")
        else:
            return self.__elements.pop()

    def peek(self):
        if self.is_empty():
            print("(empty)")
        else:
            print(self.__elements[-1])

    def is_empty(self):
        return self.__elements == []

    def size(self):
        return len(self.__elements)

    def display(self):
        print(self)

    def __str__(self):
        if self.is_empty():
            result = "(empty)"
        else:
            result = "bottom <- "
            for i in range(len(self.__elements)):
                result = result + str(self.__elements[i]) + " "
        return result


if __name__ == "__main__":
    # initialize stack
    stack = Stack()
    stack.display()

    # initialize students
    s1 = STU("Jimmy", 100)
    s2 = STU("Hardwell", 97)
    s3 = STU("Miller", 99)
    s4 = STU("Eddie", 90)
    s5 = STU("Alisa", 98)
    students = [s1, s2, s3, s4, s5]
    for i in range(len(students)):
        stack.push(students[i])
    stack.display()

    print("{} is popped".format(stack.pop()))
    stack.display()

    for i in range(4):
        stack.pop()
    stack.display()

    stack.pop()

