from threading import*
import time
s = Semaphore(3)
def wish(name):
    s.acquire()
    for i in range(3) :
        print("Good evening",end=' ')
        time.sleep(2)
        print(name)
    s.release()
begintime = time.time()

t1 = Thread(target = wish, args = {'pavan'})
t2 = Thread(target = wish, args = {'kumar'})
t3 = Thread(target = wish, args = {'karnam'})
t4 = Thread(target = wish, args = {'abc'})
t5 = Thread(target = wish, args = {'def'})
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
print(time.time()-begintime,sep = ' ')