# function with no arguments
def greet():
     print("Wellcome python classes:")
    
greet()

# fuction with 4 argument
def addnumber(a,b,c,e):
        ans=(a+b+c+e)/4;
        print(ans);
addnumber(4,6,4,8);


#power example def funtion
def power(x,y):
    for x in range(1,10):
            qub=x**3;
            print(x,"=",qub);
    
    for y in range(6,10):
          squ=y**2;
          print(" ",y,"=",squ);
        

power(1,7);

def table(x,y):
    for x in range(1,20):
            for y in range(1,11):
                  print(x,"*",y,"=",x*y);
            print(" ");      
table(1,1);


def tarrnary_op(x):
    y="even" if(x%2==0) else "odd"
    print(y)

tarrnary_op(44)

# add and fact of the n numbers

def add_fact(n):
    fact=1
    add=0
    i=1
    while(i<=n):
        add +=i
        fact *=i
        i +=1
    print(add ,"\n", fact)

add_fact(12) 

# fun of list elemetn

def list1():
    x=[1,2,3,4,5,6,3,4,53,2]
    print(len(x))
    print(type(x))
    i=0
    while(i<len(x)):
        print(x[i])
        i +=1

list1()


# lambda function 
square = lambda x: x * x
result = square(5)
print(result) 
