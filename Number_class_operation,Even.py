import math
class Number:
    def __init__(self,n):
        self.n=n
    def calculateFactorial(self):
        if self.n==0:
            return 1
        res=1
        for i in range(1,self.n+1):
            res *=i
        return res
    def checkEvenOdd(self):
        if self.n%2==0:
            return "Even"
        else:
            return "odd"
    def sumofDigits(self):
        if self.n<0:
            self.n=abs(self.n)
        temp=str(self.n)
        t=0
        for i in temp:
            t+=int(i)
        return t
    def arm(self):
        d=0
        str2=str(self.n)
        for i in str2:
            d+=math.pow(int(i),len(str2))
        if int(self.n)==d:
            return "Armstrong:"
        else:
            return "Not Armstrong"
        def prime(self):
            if self.n<1:
                return "INVALID"
            if self.n==1 or self.n==2 or self.n==3:
                return "prime number"
            for i in range(2,self,n):
                if self.n%i==0:
                    return 'Not Prime number'
            return "PRIME NUMBER"
        

inp=int(input())
obj=Number(inp)
print('Factorial of ',inp,'is',obj.calculateFactorial())
print(inp,'is',obj.checkEvenOdd())
print('sum of digits of',inp,'is',obj.sumofDigits())
print('armstrong num of',inp,'is',obj.arm())
print('prime number',inp,'is',obj.prime())

