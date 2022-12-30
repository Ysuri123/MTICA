def PrintMonth(dn):
    if(dn==1):
        return 'January'
    elif(dn==2):
        return 'February'
    elif(dn==3):
        return 'march'
    elif(dn==4):
        return 'april'
    elif(dn==5):
        return 'may'
    elif(dn==6):
        return 'june'
    elif(dn==7):
        return 'july'
    elif(dn==8):
        return 'august'
    elif(dn==9):
        return 'september'
    elif(dn==10):
        return 'october'
    
    elif(dn==11):
        return 'november'
    elif(dn==12):
        return 'december'
    
    else:
        return "invalid"
def PrintMonth1(dn):
    if(dn==0):
        return "sunday"
    if(dn==1):
        return 'Monday'
    if(dn==2):
        return 'Tuesday'
    if(dn==3):
        return 'wednsday'
    if(dn==3):
        return 'Therddy'
    
    
    if(dn==4):
        return 'Friday'
    if(dn==5):
        return 'Saterday'
    
import time    
for i in range(3):
    inpNum=int(input())
    start=time.time()
    print(PrintMonth(inpNum))
    print(time.time()-start)
    start=time.time()
    print(PrintMonth1(inpNum))
    print(time.time()-start)
