import asyncio


async def fetch_data(id, sleep_time):
    print(f'Coroutine {id} starting to fetch data...')
    await asyncio.sleep(sleep_time) # simulate a network request for IO operation

    # Return some data as a result
    return {"id": id, "data": f"Sample data from Coroutine: {id}"}


async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2, 1, 3], start = 5):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)
    
    # After the Task Group block, all tasks have completed
    
    results = [task.result() for task in tasks]
    # ta = [t for t in tasks]

    # for t in ta:
    #     print(f"{t}")

    for result in results:
        print(f'Received result: {result}')


asyncio.run(main())

"""
Coroutine 5 starting to fetch data...
Coroutine 6 starting to fetch data...
Coroutine 7 starting to fetch data...
<Task finished name='Task-2' coro=<fetch_data() done, defined at /Users/timchen2/Desktop/TakeHomeExam-by-Tim-Chen/python-asyncio-learning/asyncio-in-python-TechWithTime/task_group.py:4> result={'data': 'Sample data ... Coroutine: 5', 'id': 5}>
<Task finished name='Task-3' coro=<fetch_data() done, defined at /Users/timchen2/Desktop/TakeHomeExam-by-Tim-Chen/python-asyncio-learning/asyncio-in-python-TechWithTime/task_group.py:4> result={'data': 'Sample data ... Coroutine: 6', 'id': 6}>
<Task finished name='Task-4' coro=<fetch_data() done, defined at /Users/timchen2/Desktop/TakeHomeExam-by-Tim-Chen/python-asyncio-learning/asyncio-in-python-TechWithTime/task_group.py:4> result={'data': 'Sample data ... Coroutine: 7', 'id': 7}>
Received result: {'id': 5, 'data': 'Sample data from Coroutine: 5'}
Received result: {'id': 6, 'data': 'Sample data from Coroutine: 6'}
Received result: {'id': 7, 'data': 'Sample data from Coroutine: 7'}
"""