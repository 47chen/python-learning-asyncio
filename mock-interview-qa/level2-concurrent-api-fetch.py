"""
✅ Scenario
You're building a backend service to concurrently fetch data from 5 microservices. Speed is important — all requests should be run in parallel.

🧪 Task
Modify the following code to:
- Fetch all data concurrently
- Return results in the same order
"""


import asyncio
import time
import random

# async def fetch_data(url):

#     print(f'Start fetch... {url}')

#     await asyncio.sleep(random.uniform(0.5, 1))
#     return f'Data successfully fetched from {url}'


# # all request should be run in parallel - one await
# async def main():
#     urls = [f"https://api.service/{i}" for i in range(5)]
#     start_time = time.time()

#     # use a tasks list to wrap all the test by create task
#     # tasks = []
#     # for url in urls:
#     #     task = asyncio.create_task(fetch_data(url))
#     #     tasks.append(task)

#     tasks = [asyncio.create_task(fetch_data(url)) for url in urls]
#     # now we have a tasks with a list of tasks, we want to run it all once
#     # await 後面放awaitable object - 1. Coroutine(such as fetch_data) 2. Task(Promise) 3. Future(new Promise)
#     results = await asyncio.gather(*tasks) # 這個會回傳什麼？await Task會回傳該Task'Coroutine的return值, here as a list

#     for result in results:
#         print(result)
    
#     end_time = time.time()
#     total = end_time - start_time
#     print(f'Total time spend: {total:.2f}')

# asyncio.run(main())

async def fetch(url):
    print(f'Fetching data... from {url}')
    await asyncio.sleep(2) # simulate IO operations
    
    return f'Data successfully fetch from {url}'

async def main():
    urls = [f'https://api.service/{i}' for i in range(10)]
    # tasks = [fetch(url) for url in urls]   # Tasks => Coroutines
    tasks = []
    for url in urls:
        task = asyncio.create_task(fetch(url))
        tasks.append(task)
    
    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)

asyncio.run(main())


"""
1. asyncio.create_task only create(schedule) tasks
2. run all request in parallel (concurrently) - use asyncio.gather(*tasks)
= = = = = = = = = = = = = = = = = = = = =
https://api.service/{i}
"""