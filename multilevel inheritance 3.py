class A:
    def first_method(self):
        print("method of class A ...")
##class B:
##    def second_method(self):
##        print("Method of class B ...")

class B(A):
    def first_method(self):
        print("Method of class B ...")
        super().first_method()

ob=B()
ob.first_method()
