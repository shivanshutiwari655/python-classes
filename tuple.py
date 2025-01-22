# tuple is storing a element and it is a immutable
#creating a tuple
x=(91,2,3,4,5,2,6,7);
print(len(x));   
    # lenth of the tuple
print(x);
a=(list(x));
print(type(x));   
    # typy of the tuple
print(x);
print(x.count(2))  # find the 2 how many time is stored 
print(x)
print(x.index(4))   # where is a item stored on ondex gives a answere
print(x[1:7]) # sliceing is work possitve and negative
print(x[:7])
print(x[1:])
print(x[-9:-7])
y=1
for y in x:   # loop asseccing the tuple
    print(y)


tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('a', 'b', 'c')
tuple3 = (1, 2, 3, (4, 5))

    # Accessing elements
print("Accessing elements:", tuple1[0], tuple2[-1])

    # Slicing tuples
print("Slicing tuple1:", tuple1[1:4])

    # Tuple concatenation meens add two tuple
tuple = tuple1 + tuple2
print("Concatenated tuple:", tuple)

    # Tuple repetition
repeated = tuple2 * 3
print("Repeated tuple:", repeated)

    # Checking membership
print("Is 'a' in tuple2?:", 'a' in tuple2)
print("Is 6 in tuple1?:", 6 in tuple1)

    # Tuple length
print("Length of tuple1:", len(tuple1))

    # Tuple count (method)
tuple4 = (1, 2, 3, 1, 2, 1)
print("Count of 1 in tuple4:", tuple4.count(1))

    # Tuple index (method)
print("Index of 3 in tuple4:", tuple4.index(3))

    # Nested tuples
print("Nested tuple access (4,5):", tuple3[3])
print("Accessing nested element (5):", tuple3[3][1])

# Sorting a tuple (creates a list)
m = (3, 1, 4, 2)
n = sorted(m)
print("Sorted tuple as list:",m)

    # Min and max functions
print("Minimum value in tuple1:", min(tuple1))
print("Maximum value in tuple1:", max(tuple1))

    # Sum of tuple elements (only numeric)
print("Sum of elements in tuple1:", sum(tuple1))

    # Iterating through a tuple
print("Iterating through tuple1:")
for item in tuple1:
    print(item, end=" ")
print()
