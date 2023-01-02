def printmonth(dn):
    if dn==1:
        return 'January'
    elif dn==2:
        return 'february'
    elif dn==3:
        return 'March'
    elif dn==4:
        return 'April'
    elif dn==5:
        return 'May'
    elif dn==6:
        return 'june'
    elif dn==7:
        return 'july'
    elif dn==8:
        return 'August'
    elif dn==9:
        return 'September'
    elif dn==10:
        return 'October'
    elif dn==11:
        return 'November'
    elif dn==12:
        return 'December'
    else:
         return 'Invalid'


for i in range(3):
    inpNum=int(input())
    print(printmonth(inpNum))
