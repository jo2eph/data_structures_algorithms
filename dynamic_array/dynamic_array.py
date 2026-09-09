"""
Imlementation of a dynamic array data structure in Python.
"""

class DynamicArray:
    """
    DynamicArray class represents a dynamic array data structure,
    which automatically resizes itself when it reaches capacity.

    This data structure has an amortized O(1) time complexity for appending elements,
    and O(n) time complexity for resizing the array when it reaches capacity.
    """
    def __init__(self, capacity=1, array=None):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * self.capacity
    

    def __len__(self):
        return self.size
    

    def __repr__(self):
        return f"DynamicArray({self.array[:self.size]})"


    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.array[index]
    

    def _resize(self, new_capacity: int) -> None:
        """
        Resizes the underlying array to a new capacity
        """
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity
    

    def append(self, value) -> None:
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.size] = value
        self.size += 1
    

    def insert(self, index: int, value) -> None:
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
    


