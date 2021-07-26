# Tuples are sequences just like lists
# initialize a tuple
emptyTuple = tuple()
z = (3, 7, 4, 2)
# need the comma
tup1 = ('Michael',)
tup2 = 'Michael',
print(f"tuple 1 is {tup1}")
print(f"tuple 2 is {tup2}")
# access values in tuples
print(z[0])
print(z[-1])
# Tuple slices are similar to lists
print(z[-4:-1])
# Note that tuples are immutable
# advantages of Tuples over lists, tuples are faster than lists
# also, tuples can be dictionary keys while lists cannot
bigramsTupleDict = {('this', 'is'): 23,
                    ('is', 'a'): 12,
                    ('a', 'sentence'): 2}
print(bigramsTupleDict)
# moreover, tuples can be values in a set and lists cannot
graphicDesigner = {('this', 'is'),
                   ('is', 'a'),
                   ('a', 'sentence')}
print(graphicDesigner)

# Task: generating Fibonacci Sequence in Python
a, b = 1, 1
for i in range(10):
    print("Fib(a): ", a, "b is: ", b)
    a, b = b, a+b