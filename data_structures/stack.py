# Implementation of stack

from student import STU


class Stack:
    def __init__(self):
        self.__elements = []

    def push(self, new):
        self.__elements.append(new)

    def pop(self):
        return None if self.is_empty() else self.__elements.pop()

    def peek(self):
        return None if self.is_empty() else self.__elements[-1]

    def is_empty(self):
        return self.__elements == []

    def size(self):
        return len(self.__elements)

    def display(self):
        print(self)

    def __str__(self):
        result = "bottom <- "
        for i in range(len(self.__elements)):
            result = result + str(self.__elements[i]) + " "
        return "(empty)" if self.is_empty() else result


# Some easy tests
if __name__ == "__main__":
    # initialize stack
    stack = Stack()
    stack.display()

    # initialize students
    s1 = STU("Jimmy", 100)
    s2 = STU("Alex", 97)
    s3 = STU("Miller", 99)
    s4 = STU("Eddie", 90)
    s5 = STU("Alisa", 98)
    students = [s1, s2, s3, s4, s5]

    # Add all
    for i in range(len(students)):
        stack.push(students[i])
    stack.display()

    print("{} is popped".format(stack.pop()))
    stack.display()

    # Pop all
    for i in range(4):
        stack.pop()
    stack.display()

    # Pop on an empty stack
    if stack.pop() is None:
        print("Cannot pop from an empty stack")
