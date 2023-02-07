from threading import*
import time
l = Lock()
def wish(name):
    l.acquire()
    for i in range(3) :
        print("Good evening",end=' ')
        time.sleep(2)
        print(name)
    l.release()
begintime = time.time()

t1 = Thread(target = wish, args = {'pavan'})
t2 = Thread(target = wish, args = {'kumar'})
t3 = Thread(target = wish, args = {'karnam'})
t1.start()
t2.start()
t3.start()

print(time.time()-begintime,sep = ' ')