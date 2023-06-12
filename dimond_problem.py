class A:
    def common_method(self):
        print("This is method from class A.")


class B(A):
    def common_method(self):
        print("This is method from class B.")


class C(A):
    def common_method(self):
        print("This is method from class C.")


class D(B, C):
    pass


# Creating an instance of D
d = D()
d.common_method()
