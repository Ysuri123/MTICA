##def f():
##    x=10
##    print('id(x)in f outer:',id(x))
##    def g():
##        nonlocal x
##        x=15
##        print('id(x)in g inner:',id(x))
##    g()
##    print(x)
##f()


##def outer():
##    print('outer function')
##    def inner():
##        print('inner function')
##    inner()
##outer()


def outer():
    message='outer function'
    print('outer function')
    def inner():
        print('inner function')
    inner()
outer()

