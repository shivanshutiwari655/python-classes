# set element  is a immutable and unorderd and we are don't use in list and dict 
y=set()
x={1,2,3,6,85,3,2,1,3,4}
y={1,2,3,4,5,6,7,2,3,4}
print(type(y)) # type of the set
print(x.remove(6))  # remove a particular item
print(x.pop())   #pop the first item in set
print(x.pop())
print(x.intersection(y))  # combine of the two set but one itme is once unique
print(x.union(y))   # which item is consist of two or both set print
print(x) 
x.add(22)  #  add the particular item in our set 
print(x)
x.clear()   # clear or delet all the item in the  set
print(x)
z=y.copy()   # copy of the item in the set
print(z)