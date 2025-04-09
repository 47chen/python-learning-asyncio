import asyncio

async def fetch(name):
    print(f"Preparing {name}")
    await asyncio.sleep(1)
    print(f"Done {name}")
    return name

async def main():
    # COROUTINE VERSION
    coros = [fetch(f"coro-{i}") for i in range(3)]
    print("Created coroutine objects")
    await asyncio.sleep(2)
    print("Now awaiting coroutines...")
    await asyncio.gather(*coros)

    # TASK VERSION - 
    tasks = [asyncio.create_task(fetch(f"task-{i}")) for i in range(3)]
    print("Created and scheduled tasks")
    await asyncio.sleep(2)
    print("Now awaiting tasks...")
    await asyncio.gather(*tasks)

asyncio.run(main())

"""
Feature	Coroutines   |(fetch(...))	                  |Tasks (create_task(...))
======================================================================================
What it is	         |Just a coroutine object        |A scheduled Task (ready to run)
Executed immediately?|❌ No, just declared✅       |Yes, scheduled in event loop
Who schedules it?	 |gather() schedules it	          |You schedule it manually
Can be reused?	     |❌ No, coroutines are single-use|✅ Yes, tasks are tracked objects
Error visibility	 |Only at gather time	          |Can use .add_done_callback()


"""