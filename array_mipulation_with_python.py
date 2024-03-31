

# Python Array 
# Importing the array module
import array

# Function to create and manipulate arrays
def manipulate_array():
    """
    This function demonstrates the creation and manipulation of arrays in Python.
    """

    # Creating an array of integers
    int_array = array.array('i', [1, 2, 3, 4, 5])

    # Printing the original array
    print("Original Array:", int_array)

    # Accessing elements of the array
    print("Element at index 2:", int_array[2])

    # Modifying elements of the array
    int_array[2] = 10
    print("Modified Array:", int_array)

    # Appending new elements to the array
    int_array.append(6)
    print("Array after appending 6:", int_array)

    # Removing elements from the array
    int_array.remove(4)
    print("Array after removing 4:", int_array)

# Calling the function to demonstrate array manipulation
manipulate_array()
