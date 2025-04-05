import asyncio

"""
Semaphore works similar like Lock
- It allows multiple Coroutines to have access to the same object at the same time
"""

async def access_resource(semaphore, resource_id):
    async with semaphore:
        
        # Simulate accessing a limited resource
        print(f'Accessing resource {resource_id}')
        await asyncio.sleep(3) # Simulated work with the resource
        
        print(f'Releasing resource {resource_id}')
        print('='*50)

async def main():
    semaphore = asyncio.Semaphore(2) # Allow 2 concurrent accesses (only 2 Coroutine can access at the exact same time)
    # kind of throttle our program, we don't overload some kind of resource
    """
    Let's say we are going to send a bunch of network requests, we can do a few of them at the same time
    but we can't do maybe 1000 or 10,000 at the same time, in that case we will create "Semaphore", like maybe 5 at a time
    throttle our code to 5 request at a time
    """
    await asyncio.gather(*(access_resource(semaphore, i) for i in range(5)))

asyncio.run(main())
