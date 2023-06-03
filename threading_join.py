import threading
import time

def topla():
    sayi1 = 43
    sayi2 = 18
    print("Toplamı = " , sayi1 + sayi2)

def Carp():
    sayi1 = 43
    sayi2 = 18
    print("Carp = " , sayi1 * sayi2)

t1 = threading.Thread(target=topla)
t1.start()
t1.join()

t2 = threading.Thread(target=Carp)
t2.start()
t2.join()