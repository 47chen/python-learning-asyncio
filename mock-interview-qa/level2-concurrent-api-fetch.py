import asyncio
import time
import random

async def fetch_data(url):

    print(f'Start fetch... {url}')

    await asyncio.sleep(random.uniform(0.5, 1))
    return f'Data successfully fetched from {url}'


# all request should be run in parallel - one await
async def main():
    urls = [f"https://api.service/{i}" for i in range(5)]
    start_time = time.time()

    # use a tasks list to wrap all the test by create task
    # tasks = []
    # for url in urls:
    #     task = asyncio.create_task(fetch_data(url))
    #     tasks.append(task)

    tasks = [asyncio.create_task(fetch_data(url)) for url in urls]
    # now we have a tasks with a list of tasks, we want to run it all once
    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)
    
    end_time = time.time()
    total = end_time - start_time
    print(f'Total time spend: {total:.2f}')

asyncio.run(main())


"""
1. asyncio.create_task only create(schedule) tasks
2. run all request in parallel (concurrently) - use asyncio.gather(*tasks)
"""