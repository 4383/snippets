import os
from time import sleep
from threading import Thread
import requests

headers = {
    'User-Agent': 'thread_client',
}

def download():
    response = requests.get('http://localhost:8088', headers=headers)
    print(response.text)

threads = [
    Thread(target=download()) for i in range(5000)
]
[t.start() for t in threads]
print(f'PID = {os.getpid()}')
[t.join() for t in threads]

# python python/test_thread_client1.py  4,83s user 0,94s system 80% cpu 7,188 total
