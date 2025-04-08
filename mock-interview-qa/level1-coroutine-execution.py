"""
✅ Scenario
You’re debugging a FastAPI route and notice that some async helper functions are never run. You realize they may not be awaited or scheduled properly.

🧪 Task
Fix this code so both coroutines run properly and return their results.
"""

import asyncio
import time

async def work(name, delay):
    print(f'Work: {name} started!')
    await asyncio.sleep(delay) # simulated IO operations

    return f'Data {name} has completed with {delay} latency'

async def main():
    s = time.time()
    
    result1 = await work('Level 1', 2)
    result2 = await work('ABCDE', 3)
    
    e = time.time()
    total = e - s
    
    print(result1, f'\n{result2}')
    print(f'Total time: {total:.2f}')

asyncio.run(main())

"""
1. In order to execute Coroutine - it must be awaited!
= = = = = = = = = = =
Asnyc Feature Tested
- Coroutines & Execution




"""

# import asyncio

# async def work(name, delay):
#     print(f'{name} started...')

#     await asyncio.sleep(delay) # simulate IO operation

#     print(f'{name} done!')
#     return name


# async def main():
#     result1 = await work("B", 2)
#     result2 = await work("C", 3)
    
#     print(result1, result2) # suppose B, C


# asyncio.run(main())