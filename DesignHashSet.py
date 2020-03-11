class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__size = 1000000
        self.__data = [None] * self.__size

    def add(self, key: int) -> None:
        hash_val = key % 1000000
        self.__data[key] = key

    def remove(self, key: int) -> None:
        hash_val = key % 1000000
        if self.contains(key):
            self.__data[key] = None

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hash_val = key % 1000000
        if self.__data[key] == key:
            return True
        else:
            return False
