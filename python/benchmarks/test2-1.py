import os
from time import sleep
from threading import Thread
import requests

headers = {
    'User-Agent': 'requests_thread_client_with_session',
}

s = requests.Session()

def download(session):
    response = session.get('http://localhost:8088', headers=headers)
    print(response.text)

threads = [
    Thread(target=download(s)) for i in range(5000)
]
[t.start() for t in threads]
print(f'PID = {os.getpid()}')
[t.join() for t in threads]

# 4,45s user 0,39s system 74% cpu 6,502 total
