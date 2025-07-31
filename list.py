# abc = ["lucky",20,"jaipur",341542,True]
# print(abc[3])
# print(abc[-1])
# print(abc[2::1])


# Reference variable 
# a=["asc",4,6,8]

# b = a
# b[0] = "lucky"
# print(a,b)

# Lists are one of the most fundamental and versatile data structures in Python.
# They are ordered, mutable (changeable) sequences of items. 
# This means you can store a collection of items, the order in which you add them is preserved,
# and you can modify them after they've been created.

# What is a List?

# Think of a list as a container that can hold various items, like a shopping list or a to-do list.
# Each item in the list has a specific position, called an index.

#     Ordered: The items have a defined order, and that order will not change.
#     Mutable: You can change, add, or remove items after the list has been created.
#     Heterogeneous: Lists can contain items of different data types (integers, strings, floats, even other lists or objects)

# operations

# list1 = [1,3]
# list2 = [6,4]

#  concatenation
# combined_list = list1 + list2
# print(f"concatenated list:{combined_list}")  # output: concatenated list :[1,3,6,4]

#  repetition
# Repetition_list = list1 * 3
# print(f"Repeated list :{Repetition_list}")

# membership
# print(f"Is  2 in listl{2 in list1}")
# print(f"Is 5 not in list2{5 not in list2}")
# a=[1,2,3,[4,5]]
# print (5 in a)

# Method

# -ve index values in index method auto do a +1 for ex incert(-1, "xyz") it will add the data to -2 index
# if we give an invalid +ve index value then it will add the data in the end of the list
# if we give an invalid -ve index then it will add the data in the 0 index
# if we have multiple duplicate then the .remove method will only remove the fist accuracy



# my_list = ["apple ","banana","cherry"]

# Append

# my_list.append("lucky")
# print(f"After append:{my_list}")

# Insert
# my_list.insert(1, "grape") # Insert 'grape' at index 1
# print(f"After insert: {my_list}") # Output: After insert: ['apple', 'grape', 'banana', 'cherry', 'date']

# my_list.insert( -1, "mango")
# print(my_list)

# my_list.insert( -50, "guava")
# print(my_list)


# # Remove
# my_list.remove("banana")
# print(f"After remove: {my_list}") # Output: After remove: ['apple', 'grape', 'cherry', 'date']

# Pop (last item)
# popped_item = my_list.pop()
# print(f"Popped item (last): {popped_item}, List: {my_list}") # Output: Popped item (last): date, List: ['apple', 'grape', 'cherry']


# my_list = ["apple", "banana", "cherry", "banana"]

# # Pop (at index)
# popped_item_at_index = my_list.pop(0)
# print(f"Popped item (index 1): {popped_item_at_index}, List: {my_list}") # Output: Popped item (index 1): grape, List: ['apple', 'cherry']

# numbers = [5, 2, 8, 1, 9, 11]

# # Using .sort() (in-place)
# numbers.sort( reverse = True )

# print(numbers) 
# [11, 9, 8, 5, 2, 1]


# # Sorting a list of strings
# words = ["banana", "vipia", "apple", "cherry", "datte"]
# words.sort( reverse=True )
# print(f"Sorted words: {words}") # Output: Sorted words:  ['vipia', 'datte', 'cherry', 'banana', 'apple']

# Using sorted() (returns new list)
# new_sorted_list = sorted(numbers, reverse=True)
# print(f"New sorted list: {new_sorted_list}") # Output: New sorted list: [1, 2, 5, 8, 9]
# print(f"Original numbers after sorted(): {numbers}") # Output: Original numbers after sorted(): [5, 2, 8, 1, 9]

# sorted_list = sorted("sjhfygr4ikpok093jf09")
# print("".join(sorted_list))

# Reverse sort
# numbers.sort(reverse=True)
# print(f"Reverse sorted in-place: {numbers}") # Output: Reverse sorted in-place: [9, 8, 5, 2, 1]


# my_list = [1, 1, 1, 1, 1, 2, 1, 3, 2, 4, 2]

# print(f"Count of 2: {my_list.count(2)}") # Output: Count of 2: 3
# print(f"Count of 67: {my_list.count(67)}") # Output: Index of 4: 4

# my_list = ["apple", "banana", "cherry", "banana"]
# number_of_banana = my_list.count("banana")
# counter = 1
# while counter <= number_of_banana:
#     my_list.remove("banana")
#     counter += 1
# print(my_list)

# Index

# print(f"Index of 1: {my_list.index(1)}") # Output: Index of 1: 0
# print(f"Index of 2: {my_list.index(2)}") # Output: Index of 2: 1
# print(f"Index of 2: {my_list.index(1, 5)}") # Output: Index of 2: 1

# new_items = [5,6]
# new_list =[1,2]

# new_items = new_items + new_items

# new_items.extend(new_list)
# print (new_items)

# my_list = [1,2,3,52,"kjb"]

# my_list.reverse()
# print(f"After reverse:{my_list}")  #  output=After reverse:['kjb', 52, 3, 2, 1]


# Original = [1,2,3]
# copied = Original.copy ()


# my_list.clear()
# print(f"After clear:{my_list}")

a = {2,5,8,75,"lucky","asdf"}

# b = a.copy()
# b.pop()
# print(a)
# print(b)

a.clear()  #a= []

print(a)

counter = 1
sum = 0

while counter<=10:
    number = int(input("Enter A Number:"))
    sum +=number
    counter += 1
    print(sum)