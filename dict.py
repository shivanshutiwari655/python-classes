# dictionary is used to storing a data in key:valu pairs mutable unorderd don't allow duplicate key
x={1:"a",3:"b",4:"c","name":"shivanshu","subject":{"math":23,"english":44},"age":33,5:33};
print(type(x))
print(x)
print(x["name"])
x["name"]="alka"   # over write 
print(x)
print(x.keys())   
    # print all the keys
print(x.values())  
    # print all the value
print(x.items())   
    # print all the item key and value both
print(x.get("name3"))  
    # give the value is the same but not error if worng key entered
print(x["name"])
x.update({8:56,1:67})  
    # dict  new add or over write if key is the same so value is update
print(x)

 # Creating a second dictionary
dict1 = {"name": "shivanshu", "age": 25, "city": "satna"}

    # acessing values
print("Accessing name:", dict1["name"])

    # adding a new key-value pair
dict1["country"] = "india"
print("Dictionary after adding a key:", dict1)

    # updating a value
dict1["age"] = 26
print("Dictionary after updating a value:", dict1)

    # Removing the last key-value pair
last_item = dict1.popitem()
print("Removed last item:", last_item, "Dictionary after removal:", dict1)

    # Clearing the dictionary
dict_copy = dict1.copy()
dict1.clear()
print("Cleared dictionary:", dict1)
print("Copy of original dictionary:", dict_copy)

    # all keys
print("Keys in dict_copy:", dict_copy.keys())

    # all values
print("Values in dict_copy:", dict_copy.values())

    # Getting all items (key-value pairs)
print("Items in dict_copy:", dict_copy.items())

    # membership
print("Is 'name' in dict_copy?:", 'name' in dict_copy)

    # Default value if key not found
print("Value for gender default", dict_copy.get("gender", "Not specified"))

    # Updating dictionary
dict2 = {"profession": "Engineer", "hobby": "Reading"}
dict_copy.update(dict2)
print("Dictionary after update:", dict_copy)