# Import required libraries
import aiohttp  # Async HTTP client/server for asyncio
import asyncio  # Python's async I/O framework
import time     # For measuring execution time

async def do_request(session, url):
    """
    Async function to make a single HTTP request
    Args:
        session (aiohttp.ClientSession): The async HTTP session
        url (str): The URL to request
    Returns:
        str: The response text
    """
    # Async context manager for making the request\
    # session.get(url) => fetch(url) in js : Async http GET call
    async with session.get(url) as response:
        # session.get(url) is an async HTTP request
        print(f"{url} => {response.status}")
        return await response.text()

async def main():
    """
    Main async function demonstrating asyncio approach
    - Creates 10 identical URLs
    - Uses aiohttp for async HTTP requests
    - Creates tasks for each URL
    - Uses asyncio.gather to run all tasks concurrently
    - Single thread handles multiple I/O operations efficiently
    """
    # Create list of 10 identical URLs
    urls = ["https://example.com"] * 10
    
    # Start timing
    start_time = time.time()
    
    # Create an async HTTP session
    # async with ==> finally in JS : Manage async cleanup safely
    async with aiohttp.ClientSession() as session:
        # Create a list of tasks (coroutines) for each URL
        tasks = [do_request(session, url) for url in urls]
        # Run all tasks concurrently and wait for all to complete
        await asyncio.gather(*tasks)
        # await asyncio.gather([...]) => Promise.all([...]) in js: Runs many coroutines concurrently
    
    # End timing
    end_time = time.time()
    total_time = end_time - start_time
    print(f"\nTotal execution time with asyncio: {total_time:.2f} seconds")

if __name__ == '__main__':
    # Run the async main function
    asyncio.run(main()) 