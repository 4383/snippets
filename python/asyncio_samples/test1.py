import asyncio


async def main():
    print("Action One")
    await asyncio.sleep(1)
    print("Action Two")


if __name__ == "__main__":
    asyncio.run(main())
