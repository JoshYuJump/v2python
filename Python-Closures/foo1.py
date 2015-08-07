def foo():
    a = 1
    print id(a)
    def bar():
        # a = a + 1
        # print a + 1
        # b = a + 1
        a = 1
        print id(a)
        b = 1
        print id(b)
        print a is b
 
    bar()
    print a


foo()