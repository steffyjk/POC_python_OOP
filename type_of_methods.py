class TypeOfMethods(object):
    var = "Hello"

    def instance_method(self):
        print("This is instance method")
        print(self.var)

    @staticmethod
    def static_method():
        print("This is static method")

    @classmethod
    def class_method(cls):
        print("This is class method")
        print(cls.var)


d = TypeOfMethods()
d.class_method()
d.instance_method()
d.static_method()
