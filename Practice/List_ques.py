# Create a list with the elements: "apple", "banana", "cherry".

list = ["apple", "banana", "cherry"]

# How can you access the second element of a list?

secont_element = list[1]
print(secont_element)

# How do you change the first element of a list to "orange"?
# list[0] = "orange"
# print(li) 

# How can you find the length of a list?
print("length of list is =",len(list))


# How do you add a new element "grape" to the end of a list?

list.append("grape")
print(list)

# What method is used to insert an element at a specific position in a list?

list.insert(1, "kiwi")  # Insert "kiwi" at index 1
print(list)


# How can you remove an element by its value from a list?
list.remove("banana")
print(list)


# How do you remove an element by its index from a list?
list.pop(1)
print(list)


# What is the difference between pop() and remove() methods?

print("pop() method removes the element by index while remove () method removes element by value")


# How do you count how many times an element appears in a list?

print(list.count("grape"))



# How do you sort a list in ascending order and decending order?

list2 = [3, 1, 4, 2]

print("accending order =", sorted(list2))
print("decending order =", sorted(list2, reverse=True))


list.sort()
print(list)

