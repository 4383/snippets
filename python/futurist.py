import time

import futurist

def delayed_func():
    print("started")
    time.sleep(3)
    print("done")

e = futurist.ThreadPoolExecutor()
fut = e.submit(delayed_func)
time.sleep(1)
print("hello")
time.sleep(1)
e.shutdown()
