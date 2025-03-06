#list=[a,b,c,d]

#list operations
# Creating a list
numbers = [10, 20, 30, 40, 50]
print("Original List:", numbers)

# 1. Append an element
numbers.append(60)
print("After Append:", numbers)

# 2. Insert an element at index 2
numbers.insert(2, 25)
print("After Insert:", numbers)

# 3. Extend list with another list
numbers.extend([70, 80])
print("After Extend:", numbers)

# 4. Remove an element
numbers.remove(30)
print("After Remove:", numbers)

# 5. Pop an element (last by default)
numbers.pop()
print("After Pop:", numbers)

# 6. Pop an element at index 1
numbers.pop(1)
print("After Pop at index 1:", numbers)

# 7. Get the index of an element
index_40 = numbers.index(40)
print("Index of 40:", index_40)

# 8. Count occurrences of an element
count_50 = numbers.count(50)
print("Count of 50:", count_50)

# 9. Sort the list
numbers.sort()
print("After Sort:", numbers)

# 10. Reverse the list
numbers.reverse()
print("After Reverse:", numbers)

# 11. Copy the list
numbers_copy = numbers.copy()
print("Copied List:", numbers_copy)

# 12. Clear the list
numbers.clear()
print("After Clear:", numbers)
