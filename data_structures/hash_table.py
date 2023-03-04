# Implementation of hash table
# This implementation isn't as flexible as the other ones... due to get_key(). The others only compare keys

class Item:
    def __init__(self, key):
        self.key = key

    def __str__(self):
        return str(self.key)


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = []
        for i in range(size):
            self.table.append([])

    def hash_map(self, key):
        return key % self.size

    def is_found(self, target):
        hash_value = self.hash_map(target.key)
        return target in self.table[hash_value]

    # insert and delete are minimally implemented
    def insert(self, new):
        hash_value = self.hash_map(new.key)
        self.table[hash_value].append(new)

    def delete(self, target):
        hash_value = self.hash_map(target.key)
        self.table[hash_value].remove(target)

    def __str__(self):
        result = ''
        for i in range(self.size):
            result += "[{}]: ".format(i)
            if self.table[i] == []:
                result += "(empty)\n"
                continue
            for j in range(len(self.table[i])-1):
                result = result + str(self.table[i][j]) + " -> "
            result = result + str(self.table[i][-1]) + '\n'
        return result


if __name__ == "__main__":
    ht = HashTable(10)
    for i in range(101):
        ht.insert(Item(i))
    print(ht)


