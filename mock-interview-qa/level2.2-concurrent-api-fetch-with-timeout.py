import asyncio
import random
import time

async def fetch(url):
    print(f'Fetching... {url}')
    await asyncio.sleep(random.uniform(0.3, 3))
    return f'Data fetched successfully from {url}'


async def main():
    urls = [f"https://api.service/{i}" for i in range(10)]

    async def fetch_with_timeout(url):
        try:
            task = asyncio.wait_for(fetch(url), timeout=1.5)
            # print(task, type(task))
            return await task
        except asyncio.TimeoutError:
            return f'{url} fetched is time-out!'
    
    tasks = [fetch_with_timeout(url) for url in urls]
    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)

asyncio.run(main())


# async def main():
#     urls = [f"https://api.service/{i}" for i in range(10)]

#     async def fetch_with_timeout(url):
#         try:
#             task = await asyncio.wait_for(fetch(url), timeout=2.0)
#             print(task, type(task))
#             return task
    
#         except asyncio.TimeoutError:
#             return f"{url} timed out!"
    
#     tasks = [fetch_with_timeout(url) for url in urls]
#     results = await asyncio.gather(*tasks)

#     for r in results:
#         print(r)

# asyncio.run(main())


# https://jsonplaceholder.typicode.com/users/