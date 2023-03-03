# Implementation of hash table

class Item:
    def __init__(self, key):
        self.__key = key

    def get_key(self):
        return self.__key

    def __str__(self):
        return str(self.__key)


class HashTable:
    def __init__(self, size=10):
        self.__size = size
        self.__table = []
        for i in range(size):
            self.__table.append([])

    def hash_map(self, key):
        return key % self.__size

    def is_found(self, target):
        hash_value = self.hash_map(target.get_key())      # get_key() may vary
        return target in self.__table[hash_value]

    # insert and delete is minimally implemented
    def insert(self, new):
        hash_value = self.hash_map(new.get_key())
        self.__table[hash_value].append(new)

    def delete(self, target):
        hash_value = self.hash_map(target.get_key())
        self.__table[hash_value].remove(target)

    def __str__(self):
        result = ''
        for i in range(self.__size):
            result += "[{}]: ".format(i)
            if self.__table[i] == []:
                result += "(empty)\n"
                continue
            for j in range(len(self.__table[i])-1):
                result = result + str(self.__table[i][j]) + " -> "
            result = result + str(self.__table[i][-1]) + '\n'
        return result


if __name__ == "__main__":
    ht = HashTable(10)
    for i in range(101):
        ht.insert(Item(i))
    print(ht)


