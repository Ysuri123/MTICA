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
    
    
for i in range(3):
    inpNum=int(input())
    print(PrintMonth(inpNum))
