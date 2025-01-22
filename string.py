# string some rules for deffination
x="heelo"+ "world"  #\n for move next line
y='hello\tshivanshu'  # \t for giving a tab space
print(len(x))
print(x+ "   "+y)
print(len(x)+len(y)); # lenth of the string

# slice meens accessing smoll part of sentance
print(x[2:])
print(x[1:4]);  # a part
print(x[:9])
print(x[0:len(x)])

# nagtive indexing
print(x[5])
print(x[-9:])
print(x[:-1])
print(x[-9:-1])

# string funcatin
print(x.endswith("le"))
print(x.capitalize())
print(x.replace("e","p"))
print(x)
print(x.find("l"))
print(x.count("e"))