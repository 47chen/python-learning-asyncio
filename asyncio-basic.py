import asyncio

async def main():
    await asyncio.sleep(10)
    print('hello world')

# coroutine function needs to schedule by event loop before it can be executed

# main() - never awaited main()
asyncio.run(main())

async def worker():
    await asyncio.sleep(1)
    return 'done'

async def main2():
    task = asyncio.create_task(worker()) 
    # Task object, like a promise in NodeJS, can be wrap into asyncio.gather(*task)
    # Promise.all([task1, task2, task3...])

    result = await task
    print(result)

asyncio.run(main2())

"""
上面的code會先跑出
'hello world' after 10 second
'done' on 11 second
因為async.run 會start another eventloop, run the coroutine to completion, and then shuts down.
"""

### Real-world - combine the coroutines in one event loop
async def long_sleep():
    await asyncio.sleep(10)
    print('long_sleep 10-second done')

async def worker():
    await asyncio.sleep(1)
    print('workd 1-second done')
    return 'done'


async def main():
    # Schedule both coroutines concurrently
    task1 = asyncio.create_task(long_sleep())
    task2 = asyncio.create_task(worker())

    tasks = [task1, task2]
    await asyncio.gather(*tasks)

asyncio.run(main())

"""
workd 1-second done
long_sleep 10-second done

由於只用了一個event-loop，會優先把不需要等待的做完
"""


