#!/usr/bin/python  
# -*- coding: utf-8 -*-

import copy  
  
def printInfo(info):  
    print unicode(info, 'utf-8').encode('gbk')  
  
#拷贝接口  
class ICloneable:  
    def shallowClone(self):  
        return copy.copy(self)  
      
    def deepClone(self):  
        return copy.deepcopy(self)  
  
#工作经历  
class WorkExperience(ICloneable):  
    workData = ""  
    company = ""  
    pass  
  
#简历  
class Resume(ICloneable):  
    name = ""  
    sex = '未知'  
    age = 0  
    work = None  
      
    def __init__(self, name, work = WorkExperience()):  
        self.name = name  
        self.work = work;  
      
    def setPersonInfo(self, sex, age):  
        self.sex = sex  
        self.age = age  
      
    def setWorkExperience(self, workData, company):  
        self.work.workData = workData  
        self.work.company = company      
      
    def display(self):  
        printInfo('%s, %s, %d' % (self.name,self.sex,self.age))  
        printInfo('%s, %s' % (self.work.workData, self.work.company))  
  
def clientUI():  
    a = Resume('大鸟')  
    a.setPersonInfo('男',29)  
    a.setWorkExperience("1998-2000","XX公司")      
      
    #浅拷贝  
    b = a.shallowClone()  
    b.setWorkExperience("2000-2006","YY公司")          
      
    #深拷贝  
    c = a.deepClone()  
    c.setWorkExperience("2006-2009","ZZ公司")      
      
    b.display()  
    a.display()   
    c.display()      
    return  
  
if __name__ == '__main__':  
    clientUI();  