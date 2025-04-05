import asyncio

async def fetch_data(delay):
    print('fetching data...')
    await asyncio.sleep(delay) # Simulate an I/O operation with a sleep

    print('data fetched')
    return {'payload': 'somedata'} # return some data


async def main(): # coroutine function 
    print('Start of main coroutine')
    task = fetch_data(2)

    # Await the fetch data coroutine, pasuing execution of main until fetch_data completes
    result = await task
    print(f"--- Received result: {result}")
    print('End of main coroutine')


# main() -> Coroutine object


# Run the main coroutine
asyncio.run(main()) # pass as coroutine object