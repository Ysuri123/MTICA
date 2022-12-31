fo1=open(r"D:\pythonpractice61\day10\abc1.txt","r")
fo2=open(r"D:\pythonpractice61\day10\abc3.txt","w+")

temp=fo1.read()
fo2.write(temp)


fo1.close()
fo2.close()
print("File copied")
