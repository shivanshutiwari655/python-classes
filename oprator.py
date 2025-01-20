# 1 arithmatic oprator
x=5
y=21
print(x+y)  #addistional oprator
print(x-y)  #subbstraction oprator 
print(x*y)  #muliply oprator
print(y/x)   #divvvision oprator
print(y%x)   # modulo oprator print a reminder
print(x**y)  #power oprator

#comparison (relational) oprator
a=5
b=12
b +=10
print(a == b)  #eqqul op
print(a!=b)  # not eqqual
print(a<b)   #smoller
print(a>b)  #longer
print(a<=b)  #smoller a or eqqual
print(b)

#logical oprater
a=12
b=34
print(not (a<b)) # not operator
print(a<b or a>b) #or operator
print(a<b and a>b)   #and operator

# membership oprator
fruits=["apple","banana","mango"]
a=[2,3,4,5,6,7,8,2,4]
b=[4,6,3,54,5]
print("hello")
print("in oprator give true if the element exist : " ,"apple" in fruits) # true if element is exist in the list 
print("not in give the true if element is not exist: ",0 not in b) # true if element is not exist


print("are d and f is same? ",a is b) # true if object are same
print("Are d and f is different? " ,b is not a ) # true if object are different

# type conversion =automatic ina python and type casting
a=3
b=45
sum = a+b
print(sum)

#type casting;
a=float("45")
b=34
print(a+b)
print(type(a))

# input rules
name=input("enter your name:")
print(type(name))
print("wellcome ",name)

age=int(input("enter your age:"))
print(type(age))
print("wellcome ",age)

marks=float(input("enter your marks:"))
print(type(marks))
print("wellcome ",marks)

print("wellcome",name,"your age is",age,"and your marks is",marks);