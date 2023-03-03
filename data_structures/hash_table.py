# Implementation of hash table
# Assume we're dealing with integers only

class HashTable:
    def __init__(self, size=10):
        self.__size = size
        self.__table = [[]] * self.__size

    def hash_map(self, key):
        return key % self.__size

    def is_found(self, target):
        pass

    def insert(self, new):
        pass

    def delete(self, target):
        pass

    def __str__(self):
        pass


