from threading import*
import time
#print(threading.current_thread().getName())
def demo_thread():
    time.sleep(3)
    print("hi")

t1 = Thread(target = demo_thread())
t1.start()

