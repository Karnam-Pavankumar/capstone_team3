import time
def double(num):
    for n in num :
        time.sleep(2)
        print(2*n)
def square(num):
    for n in num :
        time.sleep(2)
        print(n*n)

n = [1,2,3,4,5]
st = time.time()
double(n)
square(n)
et = time.time()
print(et-st)

