# Implementation of queue

from student import STU


class Queue:
    def __init__(self):
        self.__elements = []

    def enqueue(self, new):
        self.__elements.append(new)

    def dequeue(self):
        return None if self.is_empty() else self.__elements.pop(0)

    def is_empty(self):
        return self.__elements == []

    def size(self):
        return len(self.__elements)

    def display(self):
        print(self)

    def __str__(self):
        if self.is_empty():
            return "(empty)"
        else:
            result = "head -> "
            for i in range(len(self.__elements)):
                result = result + str(self.__elements[i]) + " "
            result += "<- tail"
            return result


# some easy testing
if __name__ == "__main__":
    # initialize queue
    queue = Queue()
    queue.display()

    # initialize students
    s1 = STU("Jimmy", 100)
    s2 = STU("Alex", 97)
    s3 = STU("Miller", 99)
    s4 = STU("Eddie", 90)
    s5 = STU("Alisa", 98)
    students = [s1, s2, s3, s4, s5]

    # Add all
    for i in range(len(students)):
        queue.enqueue(students[i])
    queue.display()

    print("{} is dequeued".format(queue.dequeue()))
    print("{} is dequeued".format(queue.dequeue()))
    print(queue)

    while not queue.is_empty():
        queue.dequeue()

    if queue.dequeue() is None:
        print("Cannot dequeue from an empty queue")

