#encoding=utf-8  
#  
#by panda  
#组合模式  
  
  
def printInfo(info):  
    print unicode(info, 'utf-8').encode('gbk')  
  
#Component：公司抽象类  
class Company:  
    name = ''  
    def __init__(self, name):  
        self.name = name  
          
    def Add(self, company):  
        pass   
      
    def Remove(self, company):  
        pass   
      
    def Display(self, depth):  
        pass   
  
    def LineOfDuty(self): #履行职责  
        pass   
      
#Composite：公司类  
class ConcreteCompany(Company):  
    childrenCompany = None  
      
    def __init__(self, name):  
        Company.__init__(self,name)  
        self.childrenCompany = []  
          
    def Add(self, company):  
        self.childrenCompany.append(company)   
      
    def Remove(self, company):  
        self.childrenCompany.remove(company)   
      
    def Display(self, depth):  
        printInfo('-'*depth + self.name)  
          
        for component in self.childrenCompany:  
            component.Display(depth+2)  
          
  
    def LineOfDuty(self): #履行职责  
        for component in self.childrenCompany:  
            component.LineOfDuty()  
          
#Leaf：具体职能部门  
class HRDepartment(Company):     
    def __init__(self, name):  
         Company.__init__(self,name)  
       
    def Display(self, depth):  
        printInfo('-'*depth + self.name)  
      
    def LineOfDuty(self): #履行职责  
        printInfo('%s\t员工招聘培训管理' % self.name)  
   
#Leaf：具体职能部门  
class FinanceDepartment(Company):      
    def __init__(self, name):  
        Company.__init__(self,name)  
          
    def Display(self, depth):  
        printInfo('-'*depth + self.name)  
      
    def LineOfDuty(self): #履行职责  
        printInfo('%s\t公司财务收支管理' % self.name)  
  
def clientUI():      
    root = ConcreteCompany('北京总公司')  
    root.Add(HRDepartment('总公司人力资源部'))  
    root.Add(FinanceDepartment('总公司财务部'))  
      
    comp = ConcreteCompany('华东分公司')  
    comp.Add(HRDepartment('华东分公司人力资源部'))  
    comp.Add(FinanceDepartment('华东分公司财务部'))  
    root.Add(comp)  
      
    comp1 = ConcreteCompany('南京办事处')  
    comp1.Add(HRDepartment('南京办事处人力资源部'))  
    comp1.Add(FinanceDepartment('南京办事处财务部'))  
    comp.Add(comp1)  
      
    comp2 = ConcreteCompany('杭州办事处')  
    comp2.Add(HRDepartment('杭州办事处人力资源部'))  
    comp2.Add(FinanceDepartment('杭州办事处财务部'))  
    comp.Add(comp2)      
      
    printInfo('-------公司结构图-------')  
    root.Display(1)  
      
    printInfo('\n-------职责-------')  
    root.LineOfDuty()  
    return  
  
if __name__ == '__main__':  
    
    clientUI();  