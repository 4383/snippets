# examples/server_simple.py
from aiohttp import web

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

async def wshandle(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == web.WSMsgType.text:
            await ws.send_str("Hello, {}".format(msg.data))
        elif msg.type == web.WSMsgType.binary:
            await ws.send_bytes(msg.data)
        elif msg.type == web.WSMsgType.close:
            break

    return ws


def init_func(argv):
    app = web.Application()
    app.add_routes([web.get('/', handle),
                    web.get('/echo', wshandle),
                    web.get('/{name}', handle)])
    return app


if __name__ == '__main__':
    # or launch it by using:
    # python -m aiohttp.web -H localhost -P 8080 python.asyncio.test_server1:init_func
    app = init_func()
    web.run_app(app)
