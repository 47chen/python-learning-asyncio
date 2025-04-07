import asyncio

"""
Tools that allow us to synchronize the multiple Coroutines
- Lock

We want to make sure that there are no 2 Coroutines are working on this at the same time.

"""

# A shared variable
shared_resource = 0 # Maybe a table, files

# An asyncio Lock
lock = asyncio.Lock()

async def modify_shared_resource():
    global shared_resource

    # what it will do is that - it will check "Whether any other Coroutine is using the LOCK"
    # If it is, it will going to wait until that Coroutine is finished
    # If it's not, it will run the following code block
    async with lock: # <- Acquire the lock by async with lock, async context manager
        # Critical section starts
        print(f'Resource before modification: {shared_resource}')

        shared_resource += 1 # Modify the shared resource
        await asyncio.sleep(5) # Simulate an IO operation
        
        print(f'Resource after modification: {shared_resource}')
        print('='*40)
        # Critical session ends


async def main():
    # tasks = (modify_shared_resource() for _ in range(5))
    # await asyncio.gather(*tasks)
    await asyncio.gather(*(modify_shared_resource() for _ in range(5)))


asyncio.run(main())


        


"""
Resource before modification: 0 
Resource after modification: 1 - wait 5 seconds
========================================
Resource before modification: 1
Resource after modification: 2 - wait 5 seconds
========================================
Resource before modification: 2
Resource after modification: 3 - wait 5 seconds
========================================
Resource before modification: 3
Resource after modification: 4 - wait 5 seconds
========================================
Resource before modification: 4
Resource after modification: 5 - wait 5 seconds
========================================
"""

