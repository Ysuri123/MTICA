def PrintSeries(ch,n):
    sp='.'
    if n<0:
        return 'INVALID'
    else:
        for i in range(0,n):
            print(sp*(n-i-1)+ch*(2*i+1)+sp*(n-i-1))
    return None
inpch=input()
inpNum=int(input())
PrintSeries(inpch,inpNum)
