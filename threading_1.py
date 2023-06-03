import threading
import time

def func():
    print("AKMTAL")
    time.sleep(2)

zaman = time.time()

for i in range(10):
    t = threading.Thread(target=func)
    t.start()

print(time.time() - zaman)