def PrintMonth1(dn):
    if(dn==0):
        return "sunday"
    elif(dn==1):
        return 'Monday'
    elif(dn==2):
        return 'Tuesday'
    elif(dn==3):
        return 'wednsday'
    elif(dn==3):
        return 'Therddy'
    
    
    elif(dn==4):
        return 'Friday'
    elif(dn==5):
        return 'Saterday'
for i in range(3):
    inpNum=int(input())
    print(PrintMonth1(inpNum))

    
