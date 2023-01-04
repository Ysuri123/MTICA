def printsun():
    print("Sunday")
def M():
    print("Monday:")
def T():
    print("Tuesday:")
def W():
    print("Wednesday:")
def Th():
    print("Thursday")
def F():
    print("Friday:")
def S():
    print("Saturday:")
def choose():
    print("enter the number between 1-7")
daynum={1:printsun,2:M,3:T,4:W,5:Th,6:F,7:S}
choose()
while(True):
    i=int(input('Choose any one option above:'))
    if i>0 and i<8:
        daynum[i]()
    else:
        print('Invalid')
        break

            
                
