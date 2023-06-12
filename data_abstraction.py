class MyClass:
    # Hidden member of MyClass
    __hiddenVariable = 0

    def __int__(self):
        self._hide ="steff"

    # A member method that changes
    # __hiddenVariable
    def add(self, increment):
        self.__hiddenVariable += increment
        print(self.__hiddenVariable)


# Driver code
myObject = MyClass()
myObject.add(2)
myObject.add(5)

# This line causes error
# print(myObject.__hiddenVariable)
print(myObject._MyClass__hiddenVariable)
# print(myObject.__MyClass_hide)
