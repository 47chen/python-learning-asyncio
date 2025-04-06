import asyncio


async def work(name, delay):
    print(f'{name} started...')

    await asyncio.sleep(delay) # simulate IO operation

    print(f'{name} done!')
    return name


async def main():
    result1 = await work("B", 2)
    result2 = await work("C", 3)
    
    print(result1, result2) # suppose B, C


asyncio.run(main())

"""
1. In order to execute Coroutine - it must be awaited!
= = = = = = = = = = =
Asnyc Feature Tested
- Coroutines & Execution

"""