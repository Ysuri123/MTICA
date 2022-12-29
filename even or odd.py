##num1=int(input("enter a no:"))
##if num1%2==0:
##    print(num1,'is even')
##if num1%2==1:
##    print(num1,'is odd')
##print("we learnt if keyword")

####def checkEven(num1):
####    num1=int(input("enter a no:"))
####    if num1%2==0:
####        print(num1,'is even')
####    return None
####
####def checkOdd():
####    num1=int(input("enter a no:"))
####    if num1%2==1:
####        print(num1,'is odd')
####    return None
####
####checkEven()
####checkOdd()

##def checkEven(num1):
##    #str=''
##    ##num1=int(input("enter a no:"))
##    if num1%2==0:
##       ## print(num1,'is even')
##        str1=str(num1)+" is even:"
##    return str1
##
##def checkOdd(num1):
##    #num1=int(input("enter a no:"))
##    if num1%2==1:
##        #print(num1,'is odd')
##        return "odd"
##    return None
##num=int(input("Enter a no:"))
##print(checkEven(num))
##print(checkOdd(num))

def checkEvenOdd(num1):
    if num1%2==0:
        return "Even:"
    else:
        return "odd"
for i in range(3):
    num=int(input("Enter a no:"))
    print(num,"is",checkEvenOdd(num))
