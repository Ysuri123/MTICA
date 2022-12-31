fo=open(r"D:\pythonpractice61\day10\abc.txt","a")
for i in range(5):
    inpStr=input('Enter text:')
    fo.write(inpStr+'\n')

fo.close()
print('Text Written to file')
