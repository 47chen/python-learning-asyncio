import asyncio
import time

async def fetch_data(id, sleep_time):
    print (f"Coroutine {id} starting to fetch data.") 
    await asyncio.sleep(sleep_time)
    return {"id": id, "data": f"Sample data from coroutine {id}"}


async def main():
# Create tasks for running coroutines concurrently
    start_time = time.time()
    task1 = asyncio.create_task(fetch_data (1, 2))
    task2 = asyncio.create_task(fetch_data (2, 3))
    
    result1 = await task1
    result2 = await task2
    
    task3 = asyncio.create_task(fetch_data (3, 1))

    result3 = await task3
    end_time = time.time()

    total_time = end_time - start_time

    print(result1, f'\n{result2}', f'\n{result3}')
    print(f'total_time spend: {total_time:.2f}')


asyncio.run(main())


"""
A Task is to schedule a coroutine to run asap and allows us to run coroutines simultaneously
----
Coroutine 1 starting to fetch data.
Coroutine 2 starting to fetch data.
Coroutine 3 starting to fetch data.
{'id': 1, 'data': 'Sample data from coroutine 1'} 
{'id': 2, 'data': 'Sample data from coroutine 2'} 
{'id': 3, 'data': 'Sample data from coroutine 3'}
total_time spend: 3.00
"""

"""
我們也可以透過await的順序(比如先等result1, result2做完)，再run result3
這樣一來就可以控制async function的順序for our use cases
Coroutine 1 starting to fetch data.
Coroutine 2 starting to fetch data.
Coroutine 3 starting to fetch data.
{'id': 1, 'data': 'Sample data from coroutine 1'} 
{'id': 2, 'data': 'Sample data from coroutine 2'} 
{'id': 3, 'data': 'Sample data from coroutine 3'}
total_time spend: 4.00
"""