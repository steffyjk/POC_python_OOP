# OOPs Concepts in Python
# Class
# Objects
# Polymorphism
# Encapsulation
# Inheritance
# Data Abstraction

# empty class
class Name:
    pass


# demo dog class
class Dog:
    pass


# create object of class Dog
obj_dog = Dog()


# SELF in python class
# Class methods must have an extra first parameter in the method definition. We do not give a value for this parameter when we call the method, Python provides it
# If we have a method that takes no arguments, then we still have to have one argument.
# This is similar to this pointer in C++ and this reference in Java.

class Student:
    # class attribute
    student_of = "Science"

    # instance attribute
    def __init__(self, name):
        self.name = name


# OBJECT initialization
steffy = Student("Steffy")
stella = Student("Stella")

# Accessing the class attribute
print(f"steffy is a {steffy.__class__.student_of}")
print(f"steffy is a {stella.__class__.student_of}")


# Accessing the instance attribute
print(f"My name is {steffy.name}")
print(f"My name is {stella.name}")
