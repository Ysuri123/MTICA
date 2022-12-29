def div(a,b):
    assert(isinstance(a,int) or isinstance(a,float)),'Argument should be either Integer or Float'
    assert(isinstance(b,int) or isinstance(b,float)),'Second  Argument should be either Integer or Float'                 
    

                             
            
                   
    assert(b!=0),"Division by zero is not defined:"
    return a/b
try:
    print(div(55,0))
except AssertionError as obj:
    print(obj)
try:
    print(div(20,3))
except AssertionError as obj:
    print(obj)
try:
    print(div(100,20))
except AssertionError as obj:
    print(obj)
try:
    print(div(0,7))
except AssertionError as abj:
    print(obj)

