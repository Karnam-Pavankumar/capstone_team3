from threading import*
import time
def wish(name):
    for i in range(3) :
        print("Good evening",end=' ')
        time.sleep(2)
        print(name)


begintime = time.time()
t1 = Thread(target = wish, args = {'pavan'})
t2 = Thread(target = wish, args = {'kumar'})
t1.start()
t1.join()
t2.start()
t2.join()
print(time.time()-begintime,sep = ' ')