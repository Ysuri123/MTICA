def checkEvenOdd(num1):
    assert(num1>0),"Negative number"
    if num1%2==0:
        return "Even:"
    else:
        return "odd"
for i in range(3):
    num=int(input("Enter a no:"))
    try:
        print(num,"is",checkEvenOdd(num))
    except AssertionError as ob:
        print(ob)
