"""
Tests for dynamic array
"""

from dynamic_array import *

def test_dynamic_array_initialization():
    my_array = DynamicArray()
    assert len(my_array) == 0


def test_dynamic_array_append():
    my_array = DynamicArray()
    my_array.append(1)
    my_array.append(2)
    my_array.append(3)

    assert len(my_array) == 3
    assert my_array[0] == 1
    assert my_array[1] == 2
    assert my_array[2] == 3
    assert repr(my_array) == "DynamicArray([1, 2, 3])"
    assert my_array.capacity >= 3  # Capacity should be at least 3 after appending 3 elements