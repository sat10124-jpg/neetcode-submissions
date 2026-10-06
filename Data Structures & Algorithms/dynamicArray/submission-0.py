class DynamicArray:
    
    def __init__(self, capacity: int):
        self._capacity = capacity 
        self._size = 0
        self._arr = [None] * capacity

    def get(self, i: int) -> int:
        return self._arr[i]

    def set(self, i: int, n: int) -> None:
        self._arr[i] = n


    def pushback(self, n: int) -> None:
        if self._size == self._capacity:
            self.resize()
        self._arr[self._size] = n
        self._size += 1

    def popback(self) -> int:
        new_nigga = self._arr[self._size - 1]
        self._arr[self._size - 1] = None
        self._size -= 1
        return new_nigga
 

    def resize(self) -> None:
        self._capacity =  self._capacity * 2
        new_arr = [None] * self._capacity
        for i in range(self._size):
            new_arr[i] = self._arr[i]
        self._arr = new_arr


    def getSize(self) -> int:
        return self._size
        
    
    def getCapacity(self) -> int:
        return self._capacity
