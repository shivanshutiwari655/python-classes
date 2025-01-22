class student:
    name="shivanshu tiwari"
    age=22
    def __init__(self,name,marks,college):
        self.college=college
        self.marks=marks
        self.name=name
        print(self)
        print("hiii shivanshu")

    def wellcome(self):

        print("hii ssss",s1.name)


s1=student("shivanshu",44,"vits")
s1.wellcome()
s2=student("aman",77,"trs")
print(s2.marks)
print(s2.name)
print(s2.college)
print(s2.age)

print(s1.name)
print(s1.age)
print(s1)

# Encapsulation
class Person:
    def __init__(self, name, age):
        self.name = name  # Public attribute
        self.__age = age  # Private attribute (encapsulation)
    
    def display_info(self):
        return f"Name: {self.name}, Age: {self.__age}"
    
    def set_age(self, age):
        if age > 0:
            self.__age = age  # Encapsulation through getter/setter

# Inheritance
class Employee(Person):
    def __init__(self, name, age, job_title):
        super().__init__(name, age)  # Inherit from Person class
        self.job_title = job_title
    
    def display_info(self):
        return f"{super().display_info()}, Job Title: {self.job_title}"

# Polymorphism
class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Using the OOP principles
# Encapsulation example
p = Person("Alice", 30)
print(p.display_info())  # Output: Name: Alice, Age: 30
p.set_age(35)
print(p.display_info())  # Output: Name: Alice, Age: 35

# Inheritance example
e = Employee("Bob", 25, "Software Engineer")
print(e.display_info())  # Output: Name: Bob, Age: 25, Job Title: Software Engineer

# Polymorphism example
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.sound())  # Output: Bark, Meow, Some sound
