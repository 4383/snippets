import aiohttp
import asyncio

headers = {
    'User-Agent': 'aiohttp_client',
}

async def main():
    async with aiohttp.ClientSession(headers=headers) as session:
        for i in range(5000):
            async with session.get('http://localhost:8088') as response:
                html = await response.text()
                print(html[:15])

asyncio.run(main())

# python python/asyncio_samples/test_client1.py  1,41s user 0,25s system 79% cpu 2,089 total
