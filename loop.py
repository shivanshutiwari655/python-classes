# while loop example 
x=int(input("enter the number :%d\n"));
while(x<100):
    x=x+1;
    print("number is :%d\n",x);

# for loop example
x=int(input("enter the number:%d\n"));
for x in range(1,100,):
    if(x%2==0):
        print("sum number is :%d\n",x);
    else:
        print("odd number is:%d\n",x);
    #print("number is:%d\n",x);

 #nested loop esample table printing

for x in range(1,31):
    for y in range(1,11):
        print(x,"*",y,"=",x*y);
    print("\n");


 #only sum or odd number

i=1
for i in range(1,100,2):
    print(i)
    i +=1

 #fact and sum of the N numbers

i=1
n=int(input("enter the number :"))
add=0
fact=1
while(i<=n):
    print(i)
    add +=i
    fact *=i
    i +=1
print(add)
print(fact)