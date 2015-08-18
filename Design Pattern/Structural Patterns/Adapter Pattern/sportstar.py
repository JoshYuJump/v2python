#encoding=utf-8  
#  
#by panda  
#适配器模式  
  
  
def printInfo(info):  
    print unicode(info, 'utf-8').encode('gbk')  
  
#球员类  
class Player():  
    name = ''  
    def __init__(self,name):  
        self.name = name  
      
    def Attack(self,name):  
        pass  
      
    def Defense(self):  
        pass  
      
#前锋  
class Forwards(Player):  
    def __init__(self,name):  
        Player.__init__(self,name)  
      
    def Attack(self):  
        printInfo("前锋%s 进攻" % self.name)  
      
    def Defense(self,name):  
        printInfo("前锋%s 防守" % self.name)  
  
#中锋（目标类）  
class Center(Player):  
   def __init__(self,name):  
       Player.__init__(self,name)  
     
   def Attack(self):  
       printInfo("中锋%s 进攻" % self.name)  
     
   def Defense(self):  
       printInfo("中锋%s 防守" % self.name)  
     
#后卫  
class Guards(Player):  
   def __init__(self,name):  
       Player.__init__(self,name)  
     
   def Attack(self):  
       printInfo("后卫%s 进攻" % self.name)  
     
   def Defense(self):  
       printInfo("后卫%s 防守" % self.name)  
      
#外籍中锋（待适配类）  
#中锋  
class ForeignCenter(Player):  
    name = ''  
    def __init__(self,name):  
        Player.__init__(self,name)  
     
    def ForeignAttack(self):  
        printInfo("外籍中锋%s 进攻" % self.name)  
     
    def ForeignDefense(self):  
        printInfo("外籍中锋%s 防守" % self.name)  
  
  
#翻译（适配类）  
class Translator(Center):  
    foreignCenter = None  
    def __init__(self,name):  
        self.foreignCenter = ForeignCenter(name)  
     
    def Attack(self):  
        self.foreignCenter.ForeignAttack()  
     
    def Defense(self):  
        self.foreignCenter.ForeignDefense()  
  
  
def clientUI():  
    b = Forwards('巴蒂尔')  
    m = Guards('麦克格雷迪')  
    ym = Translator('姚明')  
      
    b.Attack()  
    m.Defense()  
    ym.Attack()  
    ym.Defense()  
    return  
  
if __name__ == '__main__':  
    clientUI();  