import threading
import time

def kareal(sayı):
    kare =  sayı ** 2
    print(str(sayı) + " karesi " + str(kare))
    time.sleep(1)
    print(str(kare) + " karesi " + str(kare))

zaman = time.time()

for i in range(10):
    t = threading.Thread(target=kareal,args=(i,))
    t.start()

print(time.time() - zaman)