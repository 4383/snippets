import argparse
import asyncio

import aiohttp


class AsyncClient():
    headers = {
        'User-Agent': 'async_client',
    }

    def __init__(self, number):
        self.number = number

    async def request(self, url):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            for el in range(1, self.number + 1):
                async with session.get(url) as response:
                    html = await response.text()
                    print(f"Call {el}: {html[:15]}")


class Client(AsyncClient):

    def __init__(self, number):
        self.headers = {
            'User-Agent': 'sync_client',
        }
        super().__init__(number)

    def _iter_coroutine(self, coro):
        loop = None
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            return loop.run_until_complete(coro)

    def request(self, url):
        self._iter_coroutine(super().request(url))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='the url to request')
    parser.add_argument('-n', '--number',
                        default=10, type=int,
                        help='number of time the url should be requested')
    parser.add_argument('-a', '--asynch',
                        help='setup an async client',
                        action='store_true')

    args = parser.parse_args()
    if args.asynch:
        client = AsyncClient(args.number)
        asyncio.run(client.request(args.url))
    else:
        client = Client(args.number)
        client.request(args.url)
