num1=int(input("enter a number:"))
num2=int(input("Enter a number:"))
try:
    res=num1/num2  #Execute with num2=non aero and zero #4
except ZeroDivisionError:
    print("Division by zero not allowed:")
else:
    print(num1, '/', num2, '=',res)
print('thanks')
