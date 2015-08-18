#encoding=utf-8  
#  
#by panda  
#桥接模式  
  
def printInfo(info):  
    print unicode(info, 'utf-8').encode('gbk')  
  
#抽象类：手机品牌  
class HandsetBrand():  
    soft = None  
    def SetHandsetSoft(self, soft):  
        self.soft = soft  
      
    def Run(self):  
        pass  
      
#具体抽象类：手机品牌1  
class HandsetBrand1(HandsetBrand):  
    def Run(self):  
        printInfo('手机品牌1:')  
        self.soft.Run()  
  
#具体抽象类：手机品牌2  
class HandsetBrand2(HandsetBrand):  
    def Run(self):  
        printInfo('手机品牌2:')  
        self.soft.Run()  
  
      
#功能类：手机软件  
class HandsetSoft():  
    def Run(self):  
        pass  
  
#具体功能类：游戏      
class HandsetGame(HandsetSoft):  
    def Run(self):  
        printInfo('运行手机游戏')  
          
#具体功能类：通讯录     
class HandsetAddressList(HandsetSoft):  
    def Run(self):  
        printInfo('运行手机通信录')  
  
def clientUI():  
    h1 = HandsetBrand1()  
    h1.SetHandsetSoft(HandsetAddressList())  
    h1.Run()  
    h1.SetHandsetSoft(HandsetGame())  
    h1.Run()  
      
    h2 = HandsetBrand2()  
    h2.SetHandsetSoft(HandsetAddressList())  
    h2.Run()  
    h2.SetHandsetSoft(HandsetGame())  
    h2.Run()      
    return  
  
if __name__ == '__main__':  
    clientUI();  