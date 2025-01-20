#control stetment example only if
a=int(input("enter the number:%d\n"))
if(a%2==0):
    print("this is the even number")

# 2 control stetment example if else
x=int(input("enter the number:%d\n"))
if(x>18):
    print("eligibl  for vote ")

else :
    print("not eligible for vote")

# example 3 for if else and elif
x=int(input("enter the opreter:%d\n"))
if(x<0):
    print("negetive number :\n")
elif(x>0):
    print("positve number:\n")
else:
    print("number is zero")

# example 4 many elif stetment
chemistry=int(input("enter the student marks in exam chemistry: %d\n "))
math=int(input("enter the second number maath:%d\n"))
physic=int(input ("enter the number physic:%d\n"))
hindee=int(input("enter the hindee marks"))
english=int(input("enter the english marks"))
marks=(physic+chemistry+math+hindee+english)/5
if(marks>80):
    print("topper of the class A+ grade:%d\n",marks)
elif(marks>60):
    print("pass in first divission:%d\n",marks)
elif(marks>45):
    print("pass in second divission:%d\n",marks)
elif(marks>33):
    print("pass but third divission :%d\n",marks)
else:
    print("student is fail :%d\n",marks)

# example 5 tarnary if-else statment 
z=45
y= "even" if(z%2==0) else "odd"
print(y)