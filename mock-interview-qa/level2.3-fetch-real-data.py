import asyncio
import aiohttp
import random

# async def fetch(session, user_id):
#     url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
#     try:
#         async with session.get(url) as response: # js: await fetch(url) = session.get(url)
#             await asyncio.sleep(random.uniform(0.5, 3))
#             return await response.json() 
#     except Exception as e:
#         print(f'Error fetching user {user_id}:', e)
#         return None
    
# async def get_users(user_ids):
#     # User a single session to amke all requests efficiently
#     async with aiohttp.ClientSession() as session:
#         # Create one task for each user fetch
#         tasks = [fetch(session, user_id) for user_id in user_ids] # ** why not put await before fetch?

#         # Run all tasks in the same time
#         users = await asyncio.gather(*tasks)
#         return users

# async def main():
#     user_ids = [1,2,3,4]
#     results = await get_users(user_ids)
#     for result in results:
#         print(result)

# asyncio.run(main())

async def fetch(session, url): # get_data 共享一個session by aioHttp.ClientSession() as session
    try:
        async with session.get(url) as response:
            
            await asyncio.sleep(0.1) # simulated IO 
            return await response.json()
    except Exception as e:
        print('something went wrong', e)
        return None

async def get_users(user_ids):
    url = f'https://jsonplaceholder.typicode.com/users'
    try:
        async with aiohttp.ClientSession() as session:
            coros = [asyncio.create_task(fetch(session, f'{url}/{user_id}')) for user_id in user_ids]
            
            users = await asyncio.gather(*coros)
            return users

    except Exception as e:
        print('sometime went wrong', e)
        return None

async def main():
    user_ids = [1,2,3,4]
    results = await get_users(user_ids)

    for result in results:
        print(result)

asyncio.run(main())

# url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
# session.get(url) as session =~ fetch(url) in js
# aioHttp.ClientSession as session open a session for all request to improve efficiency


