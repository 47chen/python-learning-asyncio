"""
✅ Scenario
You are handling concurrent form submissions to increment a shared counter (like Redis). You must prevent race conditions and maintain correct final value.

🧪 Task
Use a lock to safely increment the counter.
"""


import asyncio
import random

shared_counter = 0
lock = asyncio.Lock()

async def update_counter(user_id):
    # access the global variable
    global shared_counter
    
    # lock the shared resource and mock IO operation
    async with lock:
        print('=== Acquire lock for synchronize the shared resource ===')
        print(f'User:{user_id} is access the shared_counter - {shared_counter}')
        await asyncio.sleep(random.uniform(0.5, 3))
        shared_counter += 1
        print(f'User:{user_id} fininshing updating the shared_counter - {shared_counter}')
        print('=== Release the lock ===')

async def main():
    await asyncio.gather(*(update_counter(i) for i in range(10)))

asyncio.run(main())

"""
1. Use global to access the shared_resource | modify a global varaible from a function
2. Use async with lock to properly manage start/close the code block, 
   and use lock to synchronize the thread for shared resource.
"""



"""
=== Acquire lock for synchronize the shared resource ===
User:0 is access the shared_counter - 0
User:0 fininshing updating the shared_counter - 1
=== Release the lock ===
=== Acquire lock for synchronize the shared resource ===
User:1 is access the shared_counter - 1
User:1 fininshing updating the shared_counter - 2
=== Release the lock ===
=== Acquire lock for synchronize the shared resource ===
User:2 is access the shared_counter - 2
User:2 fininshing updating the shared_counter - 3
=== Release the lock ===
=== Acquire lock for synchronize the shared resource ===
User:3 is access the shared_counter - 3
User:3 fininshing updating the shared_counter - 4
=== Release the lock ===
=== Acquire lock for synchronize the shared resource ===
User:4 is access the shared_counter - 4
User:4 fininshing updating the shared_counter - 5
=== Release the lock ===
=== Acquire lock for synchronize the shared resource ===
User:5 is access the shared_counter - 5
User:5 fininshing updating the shared_counter - 6
=== Release the lock ===
=== Acquire lock for synchronize the shared resource ===
User:6 is access the shared_counter - 6
User:6 fininshing updating the shared_counter - 7
=== Release the lock ===
=== Acquire lock for synchronize the shared resource ===
User:7 is access the shared_counter - 7
User:7 fininshing updating the shared_counter - 8
=== Release the lock ===
=== Acquire lock for synchronize the shared resource ===
User:8 is access the shared_counter - 8
User:8 fininshing updating the shared_counter - 9
=== Release the lock ===
=== Acquire lock for synchronize the shared resource ===
User:9 is access the shared_counter - 9
User:9 fininshing updating the shared_counter - 10
=== Release the lock ===
"""

