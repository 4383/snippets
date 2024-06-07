from eventlet import tpool
import eventlet

def test():
    print("oh yeah 1")
    eventlet.sleep(3)
    print("oh yeah 2")


print("start")
tpool.execute(test)
print("done")
