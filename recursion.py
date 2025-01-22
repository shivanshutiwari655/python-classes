# recursive funcation 
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)


#fact of n number
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return fact(n-1)*n
    
print(fact(5))

  #access of list
def list1(list,idx=0):
    if(id==len(list)):
        return
    print(list[idx])
    list1(list,idx +1)

x=[1,3,5,3,2,5,6,4,23,5,764,3,2,5,6]
list1(x)
