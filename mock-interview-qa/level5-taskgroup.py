import asyncio

async def process(user_id):
    await asyncio.sleep(1.5) # simulat IO operation
    return f"Data is being process by {user_id}"


async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for user_id in range(5):
            task = tg.create_task(process(user_id))
            tasks.append(task)
    
    for t in tasks:
        print(t.result())

asyncio.run(main())

