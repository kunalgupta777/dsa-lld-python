import threading
import time

def func(num):
    time.sleep(2)
    print("In func using thread #", num)

if __name__ == "__main__":
    tc = 10
    threads = []
    for i in range(tc):
        threads.append(threading.Thread(target=func, args=(i+1,)))
    
    for i in range(tc):
        threads[i].start()
    
    for i in range(tc):
        threads[i].join()
    