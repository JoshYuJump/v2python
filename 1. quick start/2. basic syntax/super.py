# -*- coding: utf-8 -*-

# 在Python类的方法（method）中，要调用父类的某个方法，
# 在Python 2.2以前，通常的写法如代码段1：

# class  A():
#     def __init__(self):
#         print 'Enter A'
#         print 'Leave A'

# class B(A):
#     def __init__(self):
#         print 'Enter B'
#         A.__init__(self)
#         print 'Leave B'

# b = B() 
        
                        
# 这样的坏处是，一量 B的父类变成 C，那么得修改 B的代码

# 从 Python 2.2 之后：

class A(object):
    def __init__(self):
        print 'Enter A'
        print 'Leave A'

class B(A):
    def __init__(self):
        print 'Enter B'
        super(B, self).__init__()
        print 'Leave B'
        
b = B()                         