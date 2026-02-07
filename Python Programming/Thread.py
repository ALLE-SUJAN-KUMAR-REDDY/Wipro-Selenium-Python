# threading - execution of tasks
# multithreading - execution of many tasks at a time
# Multiprocessing -
import threading
# threading - imported

# process - execution unit
# threads - light weight unit inside the process

# simple thread

import time

def task ():
    print("Thread started")
    time.sleep(2)
    print("Thread finished")

t = threading.Thread(target = Task)
t.start()
t.join()

print("Thread terminated")

