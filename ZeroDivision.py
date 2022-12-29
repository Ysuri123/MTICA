num1=(input("enter a number:"))
num2=(input("Enter a number:"))
try:
    res=int(num1)/int(num2)  #Execute with num2=non aero and zero
except (ZeroDivisionError,ValueError):
    print("Exception handled by Manoher:")

except Exception as ob:
    print(ob)

else:
    print(num1, '/', num2, '=',res)
finally:
    print('thanks')

print("Visit again at python class at MTICA") 


