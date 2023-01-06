##i=int(input())
##if(i<1):
##    print("INVALID")
##else:
##    for a in range(1,i+1):
##        if i%a==0:
##            print(a,end=' ')
a=int(input())


def findFactor(n):
    temp=[]
    for i in range(1,n+1):
        if n%i==0:
            temp.append(i)

    return temp
print(*findFactor(a))

def findGCD(n1,n2):
    lstn1=findFactor(n1)
    lstn2=findFactor(n2)
    s1=set(lstn1)
    s2=set(lstn2)
    ans=list(s1.intersection(s2))
    ans.sort()
    return ans[-1]
print("Enter two numbers ")
a=int(input())
b=int(input())
print(findGCD(a,b))




