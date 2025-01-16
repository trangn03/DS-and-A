# Example 1: Creating a set with duplicate elements
unique_number = {1, 2, 3, 4, 5}
print("Unique numbers: ", unique_number)

# Example 2: Using set() constructor
programming_languages = set(["Python", "Java", "C++"])
print("Programming languages: ", programming_languages)

# Example 3: Creating an empty set
empty_set = set()
print("Empty set: ", empty_set)

# Example 4: Creating an imuutable set
immutable_set = frozenset([10, 20, 30])
print("Immutable set: ", immutable_set)

# Set's Methods and Operations
my_set = {1, 2, 3}
my_set.add(4)
my_set.discard(2)
print(my_set)
print(3 in my_set)

# Sets in Big O
'''
- Adding and elemnt
- Removing an element
- Checking membership
Time Complexity: O(1)
Space Complexity: O(1)
'''


