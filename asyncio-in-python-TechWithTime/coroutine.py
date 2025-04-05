import asyncio

# async def fetch_data(delay):
#     print('fetching data...')
#     await asyncio.sleep(delay) # Simulate an I/O operation with a sleep

#     print('data fetched')
#     return {'payload': 'somedata'} # return some data


# async def main(): # coroutine function 
#     print('Start of main coroutine')
#     task = fetch_data(2) # coroutine object, not yet be executed -> because it has not been awiated

#     # Await the fetch data coroutine, pasuing execution of main until fetch_data completes
#     result = await task
#     print(f"--- Received result: {result}")
#     print('End of main coroutine')


# main() -> Coroutine object

"""
In order for a coroutine to be executed, it needs be a await
"""

# Define a coroutine that simulates a time-consuming task
async def fetch_data(delay, id):
    print(f"Fetching data... id:", id)
    await asyncio.sleep(delay)  # Simulate an I/O operation with a sleep
    print("Data fetched, id:", id)
    return {"data": "Some data", "id": id}  # Return some data


# Define another coroutine that calls the first coroutine
async def main():
    task1 = fetch_data(2, 1)
    task2 = fetch_data(2, 2)

    result1 = await task1 # coroutine won't executed until it is awaited!!!!!!!!!
    print(f"Received result: {result1}")

    result2 = await task2
    print(f"Received result: {result2}") 

# Run the main coroutine
asyncio.run(main()) # pass as coroutine object

"""
Fetching data... id: 1
=== 2 second ===
Data fetched, id: 1
Received result: {"data", "Some data", "id": 1}

Fetching data... id: 2
=== 2 second ===
Data fetched, id: 2
Received result: {"data", "Some data", "id": 2}



"""
