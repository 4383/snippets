import requests
import asyncio

headers = {
    'User-Agent': 'request_asyncio_client_with_session',
}

s = requests.Session()

async def main(session):
    for i in range(5000):
        response = session.get('http://localhost:8088')
        html = response.text
        print(html[:15])

asyncio.run(main(s))

# python python/asyncio_samples/test_client1.py  1,41s user 0,25s system 79% cpu 2,089 total

