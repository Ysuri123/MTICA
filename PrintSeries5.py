def PrintSeries(n):
    
    for i in range(1,n+1):
        num=1
        print()
        for j in range(i):
            print(num,end= " ")
            num +=1
    return None
inpNum=int(input())
PrintSeries(inpNum)
            