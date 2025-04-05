import asyncio


async def fetch_data(id, sleep_time):
    print(f'Coroutine {id} starting to fetch data...')
    await asyncio.sleep(sleep_time) # simulate a network request for IO operation

    # Return some data as a result
    return {"id": id, "data": f"Sample data from Coroutine: {id}"}


async def main():
    # Run Coroutine concurrently and gather their return values
    results = await asyncio.gather(fetch_data(1,2), fetch_data(2,1), fetch_data(3,3))

    # Process the results
    for result in results:
        print(f'{result}')


# Run the coroutine function
asyncio.run(main())
"""
Coroutine 1 starting to fetch data...
Coroutine 2 starting to fetch data...
Coroutine 3 starting to fetch data...
{'id': 1, 'data': 'Sample data from Coroutine: 1'}
{'id': 2, 'data': 'Sample data from Coroutine: 2'}
{'id': 3, 'data': 'Sample data from Coroutine: 3'}
"""