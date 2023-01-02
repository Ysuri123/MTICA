def pattern(s,n):
    assert(n>=0),"INVALID"
    for i in range(n,0,-1):
        print(s*i)
s=input()
n=int(input())
#pattern(s,n)
try:
    pattern(s,n)
except AssertionError as a:
    print(a)
