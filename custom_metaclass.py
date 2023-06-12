# # def test_method(self):
# #     print("This is Test class method!")
# #
# # # creating a base class
# # class Base:
# #     def myfun(self):
# #         print("This is inherited method!")
# #
# # # Creating Test class dynamically using
# # # type() method directly
# # Test = type('Test', (Base, ), dict(x="atul", my_method=test_method))
# #
# # # Print type of Test
# # print("Type of Test class: ", type(Test))
# #
# # # Creating instance of Test class
# # test_obj = Test()
# # print("Type of test_obj: ", type(test_obj))
# #
# #
# # # calling inherited method
# # test_obj.myfun()
# #
# # # calling Test class method
# # test_obj.my_method()
# #
# # # printing variable
# # print(test_obj.x)
# #
#
# class MyMeta(type):
#     def __new__(cls, name, bases, attrs):
#         # Customize class creation here
#         # Modify attributes or perform additional operations
#
#         # Create the class object
#         cls_obj = super().__new__(cls, name, bases, attrs)
#
#         # Additional customization, if needed
#
#         # Return the created class object
#         return cls_obj
#
#
# # Example usage
# class MyClass(metaclass=MyMeta):
#     attr = "Example attribute"
#
#     def method(self):
#         return "Example method"
#
#
# # Creating an instance of MyClass
# obj = MyClass()
# print(obj.attr)
# print(obj.method())

class Meta(type):

    def __new__(self, class_name, bases, args):
        print("===", args)
        a = {}
        for name, value in args.items():
            if name.startswith("__"):
                a[name] = value
            a[name.upper()] = value

        print("-->", a)
        return type(class_name, bases, a)


class Dog(metaclass=Meta):
    x = 1
    y = 2

    def pe(self):
        print(f"hi")


c = Dog()
print(c.X)
