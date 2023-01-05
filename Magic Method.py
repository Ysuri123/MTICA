class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def __add__(self,ob):
        temp=self.real+ob.real,ob.real+ob.imag
        return temp
    def __str__(self):
        return(self.real,self.imag)
ob1=Complex(3,5)
ob2=Complex(2,1)
#ob3=ob1.add(ob2)
ob3=ob1+ob2
##print(ob3.real)
##print(ob3.img)
print(ob3)
