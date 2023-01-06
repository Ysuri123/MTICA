z=input().split()
y=input().split()
lst=[]
for i,j in zip(z,y):
    lst.append(int(i)+int(j))
print(*lst)
   
