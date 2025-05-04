# Base class A
class A:
    def show(self):
        print("Showing from class A")

# Class B inherits from A and overrides show()
class B(A):
    def show(self):
        print("Showing from class B")

# Class C inherits from A and overrides show()
class C(A):
    def show(self):
        print("Showing from class C")

# Class D inherits from both B and C
class D(B, C):
    pass

# Create an object of class D
d = D()

# Call the show method
d.show()

# To see the Method Resolution Order (MRO)
print(D.mro())