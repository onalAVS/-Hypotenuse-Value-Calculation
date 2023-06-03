import threading
import time

pi = 3.145

def kure(yarıcap):
    alan = (2/3) * pi * yarıcap ** 3
    hacmi = (4/3) * pi * yarıcap ** 3
    print("Kürenin alanı {} , Kürenin hacmi {} .".format(alan,hacmi))
    
def kup(kenar):
    alan = 6*kenar**2
    hacmi = 6*kenar**3
    print("Küpün alanı {} , Küpün hacmi {} .".format(alan,hacmi))
    
def silindir(yarıcap,yukseklik):
    alan = 2 * pi * yarıcap * yukseklik
    hacmi = pi * yarıcap * yukseklik ** 2
    print("Silindirin alanı {} , Silindirin hacmi {} .".format(alan,hacmi))

t1 = threading.Thread(target=kure,args=(8,))
t2 = threading.Thread(target=kup,args=(12,))
t3 = threading.Thread(target=silindir,args=(5,12))
lock = threading.Lock()
lock.acquire()

t1.start()
lock.acquire(blocking=True, timeout=3)

t2.start()
lock.acquire(blocking=True, timeout=3)

t3.start()
lock.acquire(blocking=True, timeout=5)