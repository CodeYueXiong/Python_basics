# Define a list
z = [3, 7, 4, 2]
# Also can contain elements with different types
DifferentElements = [3, True, 'Michael', 2.0]

# Access a value in a list
print(z[-1])  # print the last one

# Slice of a list
print(z[0:2])  # print 2 values
print(z[:3])
print(z[1:])

## List methods
# index method
print(z.index(4))
# count method
print(z.count(7))
# sort method
z1 = z
z1.sort(reverse=True)
print(z1)
# append method
z1.append(5)
print(z1)
# remove method
z1.remove(5)
print(z1)
# pop method
z1.pop(1)
print(z1)
# extend method
z1.extend([6,8])
print(z1)
# insert method
z1.insert(4, [1,2])
print(z1)