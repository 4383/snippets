import os
import asyncio


async def poc(delay=60):
    await asyncio.sleep(delay)


async def main():
    async with asyncio.TaskGroup() as tg:
        for i in range(5000):
            tg.create_task(poc(60))

print(f'PID = {os.getpid()}')
asyncio.run(main())
