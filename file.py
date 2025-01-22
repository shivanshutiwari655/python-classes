f = open('example.txt','r+')
data = f.write("")
print(data)

# 1. Create and write to a file
open("example.txt", "w")

data=f.write("This is the first line.\nThis is the second line.")
print("File created and written",data)

# 2. Read the file
f=open("example.txt", "r")
data=f.read()
print(data)

#read line by line
file = open("example.txt", "r")
for line in file:
    print(line.strip())  # Strip removes extra whitespace
file.close()

# read specific number
file = open("example.txt", "r")
print(file.read(10))  # Reads the first 10 characters
file.close()

print("hello/n");


# 3. Append to the File
with open("example.txt", "a") as file:
    file.write("\nThis is an appended line.")
print("\nAppended new content to the file.")

# 4. Read the Updated File
with open("example.txt", "r") as file:
    print("\nUpdated file content:")
    print(file.read())
