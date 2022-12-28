####ans=[]
####for i in range(1200,2000,130):
####    ans.append(i)
####print(ans)
####
##
##lst=[10,15,20,25,30,35,40,45]
##ans=[]
##for i in lst:
##    ans.append(i+6)
##print(ans)

##
##list=[10,15,20,25,30,35,40,45]
##ans=[i*i for i in list]
##print(ans)
##

##squere root

##list=[10,15,20,25,30,35,40,45]
##ans=[round(i**0.5,4) for i in list]
##print(ans)

##list=[10,15,20,25,30,35,40,45]
##ans=[]
##for i in list:
##    if i*i>50:
##        ans.append(i*i)
##print(ans)      
##        
        
list=[10,15,20,25,30,35,40,45]
ans=[i*i for i in list if i*i>50]

print(ans)      
        
