# -*- coding: utf-8 -*-
# Python面试题：请写出一段Python代码实现删除一个list里面的重复元素

l = [1, 3, 2, 'a', 'z', 'd', 3, 'd', 'z']

# set 
print list(set(l))

# dict
print {}.fromkeys(l).keys()

