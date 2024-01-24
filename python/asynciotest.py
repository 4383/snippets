import asyncio


async def f():
    try:
        while True:
            await asyncio.sleep(0)
    except asyncio.CancelledError:
        print('I was cancelled!')
    else:
        return 111

coro = f()
try:
    coro.send(None)
    coro.send(None)
    coro.throw(asyncio.CancelledError)
except StopIteration as e:
    print(f"result: {e.value}")
