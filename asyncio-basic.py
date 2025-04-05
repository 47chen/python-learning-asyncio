import asyncio

async def main():
    await asyncio.sleep(1)
    print('hello world')

# coroutine function needs to schedule by event loop before it can be executed

# main() - never awaited main()
asyncio.run(main())