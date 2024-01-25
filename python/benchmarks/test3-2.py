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

# 4,30s user 0,27s system 75% cpu 6,096 total
