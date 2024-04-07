class A:
    def disp(self):
        print("This  is from A")
class B(A):
    def disp(self):
        print("This is from B")
        super().disp()

class C(A):
    def disp(self):
        print("This is from C")
        super().disp()

class D(B,C):
    pass

obj=D()
obj.disp()
        