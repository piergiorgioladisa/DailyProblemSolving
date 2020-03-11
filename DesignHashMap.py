class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__size = 1000000
        self.__data = [-1] * self.__size

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_val = key % 1000000
        self.__data[hash_val] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_val = key % 1000000
        if self.__data[hash_val] != None:
            return self.__data[hash_val]
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_val = key % 1000000
        if self.__data[hash_val] != -1:
            self.__data[hash_val] = -1
        
