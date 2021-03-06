# -*- coding: utf-8 -*-
import time  
import thread  

mylock = thread.allocate_lock()  #Allocate a lock  

def timer(no, interval): 
    cnt = 0  
    while cnt < 10:  
        print 'Thread:(%d) Time:%s\n'%(no, time.ctime())  
        time.sleep(interval)  
        cnt+=1  
    thread.exit_thread()  
     
   
def test(): #Use thread.start_new_thread() to create 2 new threads 
    thread.start_new_thread(timer, (1,1)) 
    thread.start_new_thread(timer, (2,2)) 
    time.sleep(1)  
   
if __name__=='__main__':  
    test()  
