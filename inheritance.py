# Parent class
class Person(object):

    # __init__ is a constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(f"person name {self.name}")
        print(f"person idnumber {self.idnumber}")

    def details(self):
        print(f"My name is: {self.name}")
        print(f"Id number: {self.idnumber}")

    def say_hello(self):
        print("hello world!!")


# Child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of parent class
        Person.__init__(self, name, idnumber)

    def details(self):
        print(f"My name is: {self.name}")
        print(f"Id number: {self.idnumber}")
        print(f"Post: {self.post}")


ritik = Employee("Ritik", 123, 125, "SE")

ritik.details()
ritik.display()


class demo(Person):
    def __init__(self, a):
        self.a = a


    def image(self):
        print(f"image: ", self.a)


ans = demo(a=12)
ans.image()
ans.say_hello()
print("----------")
