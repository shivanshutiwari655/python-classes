#list example [list] is changeable muteble duble value cantion index bassed;
x=[1,2,3,4,6,5,4,2.3,6,2,3,2,4,78]
print(type(x))
print(x)
print(x[1:8:2])
x.append(77)  #add the item at the end
print(x)
x.pop();    # delet the item at the particular index or end by defolt
print(x)
x.sort()  # arange the item in assending order 
print(x)
x.sort(reverse=True);   # arange the item in desending order 
print(x)
x.remove(2); #delet the ekement 
print(x)
y=[2,5,8,3,5,6]
y.reverse();  # reverse the list but not set
print(y)
del(x[2])   #delet the item in partcular index
print(x)
y=[3,5,6,8,9]
x.extend(y);  # add the another list in end of the list
print(x)
z=x.copy() # coppy the all item in  a list
print(z)
x.sort()
print(x)
lenth=(len(x)); #find the lenth of the list 
print(lenth)
i=1

#Iterating through a list
for item in x:  
    print("the number is ans",i,"and",item);
    i +=1
while (i<len(x)):
    print(i)
    i +=1
x.reverse()
print(x)


# Slicing lists
print("Slicing list1:", x[1:8])

    # Modifying elements
x[0] = 10
print("Modified list1:", x)


